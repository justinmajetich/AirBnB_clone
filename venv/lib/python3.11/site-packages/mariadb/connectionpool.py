#
# Copyright (C) 2020-2021 Georg Richter and MariaDB Corporation AB

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Library General Public
# License as published by the Free Software Foundation; either
# version 2 of the License, or (at your option) any later version.

# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Library General Public License for more details.

# You should have received a copy of the GNU Library General Public
# License along with this library; if not see <http://www.gnu.org/licenses>
# or write to the Free Software Foundation, Inc.,
# 51 Franklin St., Fifth Floor, Boston, MA 02110, USA
#

import mariadb
import _thread
import time

from mariadb.constants import STATUS

MAX_POOL_SIZE = 64


class ConnectionPool(object):
    """
    Class defining a pool of database connections

    MariaDB Connector/Python supports simple connection pooling.
    A connection pool holds a number of open connections and handles
    thread safety when providing connections to threads.

    The size of a connection pool is configurable at creation time,
    but cannot be changed afterwards. The maximum size of a connection
    pool is limited to 64 connections.

    Keyword Arguments:

        * pool_name (str) -- Name of connection pool

        * pool_size (int)=5 -- Size of pool. If not specified default value
          of 5 will be used. Maximum allowed number is 64.

        * pool_reset_connection (bool)=True -- Will reset the connection before
          returning it to the pool.  Default value is True.

        * pool_validation_interval (int)=500 -- Specifies the validation
          interval in milliseconds after which the status of a connection
          requested from the pool is checked.
          The default values is 500 milliseconds, a value of 0 means that
          the status will always be checked.
          (Added in version 1.1.6)
    """

    def __init__(self, *args, **kwargs):
        """
        Creates a connection pool class

        :param str pool_name:
            Name of connection pool

        :param int pool_size:
            Size of pool. If not specified default value of 5 will be used.
            Maximum allowed number is 64.

        :param bool pool_reset_connection:
            Will reset the connection before returning it to the pool.
            Default value is True.
        """
        self._connections_free = []
        self._connections_used = []
        self._pool_args = {}
        self._conn_args = {}
        self._lock_pool = _thread.RLock()
        self.__closed = 0

        key_words = ["pool_name", "pool_size", "pool_reset_connection",
                     "pool_validation_interval"]

        # check if pool_name was provided
        if kwargs and "pool_name" in kwargs:

            # check if pool_name already exists
            if kwargs["pool_name"] in mariadb._CONNECTION_POOLS:
                raise mariadb.ProgrammingError("Pool '%s' already exists"
                                               % kwargs["pool_name"])
        else:
            raise mariadb.ProgrammingError("No pool name specified")

        # save pool keyword arguments
        self._pool_args["name"] = kwargs.get("pool_name")
        self._pool_args["size"] = int(kwargs.get("pool_size", 5))
        self._pool_args["reset_connection"] = \
            bool(kwargs.get("pool_reset_connection", True))
        self._pool_args["validation_interval"] = \
            int(kwargs.get("pool_validation_interval", 500))

        # validate pool size (must be in range between 1 and MAX_POOL_SIZE)
        if not (0 < self._pool_args["size"] <= MAX_POOL_SIZE):
            raise mariadb.ProgrammingError("Pool size must be in range of "
                                           "1 and %s" % MAX_POOL_SIZE)

        # store pool and connection arguments
        self._conn_args = kwargs.copy()
        for key in key_words:
            if key in self._conn_args:
                del self._conn_args[key]

        if len(self._conn_args) > 0:
            with self._lock_pool:
                # fill connection pool
                for i in range(0, self._pool_args["size"]):
                    try:
                        connection = mariadb.Connection(**self._conn_args)
                    except mariadb.Error:
                        # if an error occurred, close all connections
                        # and raise exception
                        for j in range(0, len(self._connections_free)):
                            try:
                                self._connections_free[j].close()
                            except mariadb.Error:
                                # connect failed, so we are not
                                # interested in errors
                                # from close() method
                                pass
                            del self._connections_free[j]
                        raise
                    self.add_connection(connection)

        # store connection pool in _CONNECTION_POOLS
        mariadb._CONNECTION_POOLS[self._pool_args["name"]] = self

    def _replace_connection(self, connection):
        """
        Removes the given connection and adds a new connection.
        """

        if connection:
            if connection in self._connections_free:
                x = self._connections_free.index(connection)
                del self._connections_free[x]
            elif connection in self._connections_used:
                x = self._connections_used.index(connection)
                del self._connections_used[x]

            connection._Connection__pool = None
            connection.close()
        return self.add_connection()

    def __repr__(self):
        if (self.__closed):
            return "<mariadb.connectionPool.ConnectionPool object (closed) "\
                   "at %s>" % (hex(id(self)),)
        else:
            return "<mariadb.connectionPool.ConnectionPool object (name=%s) "\
                   "at %s>" % (self.pool_name, hex(id(self)))

    def add_connection(self, connection=None):
        """
        Adds a connection object to the connection pool.

        In case that the pool doesn’t have a free slot or is not configured
        a PoolError exception will be raised.
        """

        if not self._conn_args:
            raise mariadb.PoolError("Couldn't get configuration for pool %s" %
                                    self._pool_args["name"])

        if (connection is not None and
                not isinstance(connection, mariadb.connections.Connection)):
            raise mariadb.ProgrammingError("Passed parameter is not a "
                                           "connection object")

        if connection is None and len(self._conn_args) == 0:
            raise mariadb.PoolError("Can't get configuration for pool %s" %
                                    self._pool_args["name"])

        total = len(self._connections_free + self._connections_used)
        if total >= self._pool_args["size"]:
            raise mariadb.PoolError("Can't add connection to pool %s: "
                                    "No free slot available (%s)." %
                                    (self._pool_args["name"],
                                     total))

        with self._lock_pool:
            if connection is None:
                connection = mariadb.Connection(**self._conn_args)

            connection._Connection__pool = self
            connection.__last_used = time.perf_counter_ns()
            self._connections_free.append(connection)
            return connection

    def get_connection(self):
        """
        Returns a connection from the connection pool or raises a PoolError
        exception if a connection is not available.
        """

        conn = None

        with self._lock_pool:
            for i in range(0, len(self._connections_free)):
                conn = self._connections_free[i]
                dt = (time.perf_counter_ns() - conn.__last_used) / 1000000
                if dt > self._pool_args["validation_interval"]:
                    try:
                        conn.ping()
                    except mariadb.Error:
                        conn = self._replace_connection(conn)
                        if not conn:
                            continue

                conn._used += 1
                self._connections_used.append(conn)
                idx = self._connections_free.index(conn)
                del self._connections_free[idx]
                return conn

        raise mariadb.PoolError("No connection available")

    def _close_connection(self, connection):
        """
        Returns connection to the pool. Internally used
        by connection object.
        """
        with self._lock_pool:

            try:
                if self._pool_args["reset_connection"]:
                    connection.reset()
                elif connection.server_status & STATUS.IN_TRANS:
                    connection.rollback()
            except mariadb.Error:
                self._replace_connection(connection)

            if connection:
                if connection in self._connections_used:
                    x = self._connections_used.index(connection)
                    del self._connections_used[x]
                    connection.__last_used = time.perf_counter_ns()
                    self._connections_free.append(connection)

    def set_config(self, **kwargs):
        """
        Sets the connection configuration for the connection pool.
        For valid connection arguments check the mariadb.connect() method.

        Note: This method doesn't create connections in the pool.
        To fill the pool one has to use add_connection() ḿethod.
        """

        self._conn_args = kwargs

    def close(self):
        """Closes connection pool and all connections."""
        try:
            for c in (self._connections_free + self._connections_used):
                c._Connection__pool = None
                c.close()
        finally:
            self._connections_free = None
            self._connections_used = None
            del mariadb._CONNECTION_POOLS[self._pool_args["name"]]

    @property
    def pool_name(self):
        """Returns the name of the connection pool."""

        return self._pool_args["name"]

    @property
    def pool_size(self):
        """Returns the size of the connection pool."""

        return self._pool_args["size"]

    @property
    def max_size(self):
        "Returns the maximum size for connection pools."""

        return MAX_POOL_SIZE

    @property
    def connection_count(self):
        "Returns the number of connections in connection pool."""

        try:
            return len(self._connections_free + self._connections_used)
        except Exception:
            return 0

    @property
    def pool_reset_connection(self):
        """
        If set to true, the connection will be reset on both client and server
        side after .close() method was called
        """
        return self._pool_args["reset_connection"]

    @pool_reset_connection.setter
    def pool_reset_connection(self, reset):
        self._pool_args["reset_connection"] = reset
