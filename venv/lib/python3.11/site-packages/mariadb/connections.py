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
import socket
import mariadb.cursors

from mariadb.constants import STATUS, TPC_STATE, INFO
from packaging import version

_DEFAULT_CHARSET = "utf8mb4"
_DEFAULT_COLLATION = "utf8mb4_general_ci"
_MAX_TPC_XID_SIZE = 64


class Connection(mariadb._mariadb.connection):
    """
    MariaDB Connector/Python Connection Object

    Handles the connection to a MariaDB or MySQL database server.
    It encapsulates a database session.

    Connections are created using the method mariadb.connect()
    """

    def _check_closed(self):
        if self._closed:
            raise mariadb.ProgrammingError("Invalid connection or "
                                           "not connected")

    def __init__(self, *args, **kwargs):
        """
        Establishes a connection to a database server and returns a connection
        object.
        """

        self._socket = None
        self._used = 0
        self._last_executed_statement = None
        self._socket = None
        self.__pool = None
        self.__last_used = 0
        self.tpc_state = TPC_STATE.NONE
        self._xid = None

        autocommit = kwargs.pop("autocommit", False)
        reconnect = kwargs.pop("reconnect", False)
        self._converter = kwargs.pop("converter", None)

        # if host contains a connection string or multiple hosts,
        # we need to check if it's supported by Connector/C
        if "host" in kwargs:
            host = kwargs.get("host")
            if version.Version(mariadb.mariadbapi_version) <\
               version.Version('3.3.0') and ',' in host:
                raise mariadb.ProgrammingError("Host failover list requires "
                                               "MariaDB Connector/C 3.3.0 "
                                               "or newer")

        # compatibility feature: if SSL is provided as a dictionary,
        # we will map it's content
        if "ssl" in kwargs and not isinstance(kwargs["ssl"], bool):
            ssl = kwargs.pop("ssl", None)
            for key in ["ca", "cert", "capath", "key", "cipher"]:
                if key in ssl:
                    kwargs["ssl_%s" % key] = ssl[key]
            kwargs["ssl"] = True

        super().__init__(*args, **kwargs)
        self.autocommit = autocommit
        self.auto_reconnect = reconnect

    def cursor(self, cursorclass=mariadb.cursors.Cursor, **kwargs):
        """
        Returns a new cursor object for the current connection.

        If no cursorclass was specified, a cursor with default mariadb.Cursor
        class will be created.

        Optional keyword parameters:

        - buffered = True
          If set to False the result will be unbuffered, which means before
          executing another statement with the same connection the entire
          result set must be fetched.
          Please note that the default was False for MariaDB Connector/Python
          versions < 1.1.0.

        - dictionary = False
          Return fetch values as dictionary.

        - named_tuple = False
          Return fetch values as named tuple. This feature exists for
          compatibility reasons and should be avoided due to possible
          inconsistency.

        - cursor_type = CURSOR.NONE
          If cursor_type is set to CURSOR.READ_ONLY, a cursor is opened
          for the statement invoked with cursors execute() method.

        - prepared = False
          When set to True cursor will remain in prepared state after the first
          execute() method was called. Further calls to execute() method will
          ignore the sql statement.

        - binary = False
          Always execute statement in MariaDB client/server binary protocol.

        In versions prior to 1.1.0 results were unbuffered by default,
        which means before executing another statement with the same
        connection the entire result set must be fetched.

        fetch* methods of the cursor class by default return result set values
        as a tuple, unless named_tuple or dictionary was specified.
        The latter one exists for compatibility reasons and should be avoided
        due to possible inconsistency in case two or more fields in a result
        set have the same name.

        If cursor_type is set to CURSOR.READ_ONLY, a cursor is opened for
        the statement invoked with cursors execute() method.
        """
        self._check_closed()
        cursor = cursorclass(self, **kwargs)
        if not isinstance(cursor, mariadb._mariadb.cursor):
            raise mariadb.ProgrammingError("%s is not an instance of "
                                           "mariadb.cursor" % cursor)
        return cursor

    def close(self):
        self._check_closed()
        if self._Connection__pool:
            self._Connection__pool._close_connection(self)
        else:
            super().close()

    def __enter__(self):
        self._check_closed()
        "Returns a copy of the connection."

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._check_closed()
        "Closes connection."

        self.close()

    def commit(self):
        """
        Commit any pending transaction to the database.
        """

        self._check_closed()
        if self.tpc_state > TPC_STATE.NONE:
            raise mariadb.ProgrammingError("commit() is not allowed if "
                                           "a TPC transaction is active")
        self._execute_command("COMMIT")
        self._read_response()

    def rollback(self):
        """
        Causes the database to roll back to the start of any pending
        transaction

        Closing a connection without committing the changes first will
        cause an implicit rollback to be performed.
        Note that rollback() will not work as expected if autocommit mode
        was set to True or the storage engine does not support transactions."
        """

        self._check_closed()
        if self.tpc_state > TPC_STATE.NONE:
            raise mariadb.ProgrammingError("rollback() is not allowed if a "
                                           "TPC transaction is active")
        self._execute_command("ROLLBACK")
        self._read_response()

    def kill(self, id: int):
        """
        This function is used to ask the server to kill a database connection
        specified by the processid parameter.

        The connection id can be be retrieved by SHOW PROCESSLIST sql command.
        """

        self._check_closed()
        if not isinstance(id, int):
            raise mariadb.ProgrammingError("id must be of type int.")
        stmt = "KILL %s" % id
        self._execute_command(stmt)
        self._read_response()

    def begin(self):
        """
        Start a new transaction which can be committed by .commit() method,
        or cancelled by .rollback() method.
        """
        self._check_closed()
        self._execute_command("BEGIN")
        self._read_response()

    def select_db(self, new_db: str):
        """
        Gets the default database for the current connection.

        The default database can also be obtained or changed by database
        attribute.
        """

        self._check_closed()
        self.database = new_db

    def get_server_version(self):
        """
        Returns a tuple representing the version of the connected server in
        the following format: (MAJOR_VERSION, MINOR_VERSION, PATCH_VERSION)
        """

        return self.server_version_info

    def show_warnings(self):
        """
        Shows error, warning and note messages from last executed command.
        """

        self._check_closed()
        if (not self.warnings):
            return None

        cursor = self.cursor()
        cursor.execute("SHOW WARNINGS")
        ret = cursor.fetchall()
        del cursor
        return ret

    class xid(tuple):
        """
        xid(format_id: int, global_transaction_id: str, branch_qualifier: str)

        Creates a transaction ID object suitable for passing to the .tpc_*()
        methods of this connection.

        Parameters:

        - format_id: Format id. If not set default value `0` will be used.

        - global_transaction_id: Global transaction qualifier, which must be
          unique. The maximum length of the global transaction id is
          limited to 64 characters.

        - branch_qualifier: Branch qualifier which represents a local
          transaction identifier. The maximum length of the branch qualifier
          is limited to 64 characters.

        """
        def __new__(self, format_id, transaction_id, branch_qualifier):
            if not isinstance(format_id, int):
                raise mariadb.ProgrammingError("argument 1 must be int, "
                                               "not %s",
                                               type(format_id).__name__)
            if not isinstance(transaction_id, str):
                raise mariadb.ProgrammingError("argument 2 must be str, "
                                               "not %s",
                                               type(transaction_id).__mane__)
            if not isinstance(branch_qualifier, str):
                raise mariadb.ProgrammingError("argument 3 must be str, "
                                               "not %s",
                                               type(transaction_id).__name__)
            if len(transaction_id) > _MAX_TPC_XID_SIZE:
                raise mariadb.ProgrammingError("Maximum length of "
                                               "transaction_id exceeded.")
            if len(branch_qualifier) > _MAX_TPC_XID_SIZE:
                raise mariadb.ProgrammingError("Maximum length of "
                                               "branch_qualifier exceeded.")
            if format_id == 0:
                format_id = 1
            return super().__new__(self, (format_id,
                                          transaction_id,
                                          branch_qualifier))

    def tpc_begin(self, xid):
        """
        Parameter:
          xid: xid object which was created by .xid() method of connection
               class

        Begins a TPC transaction with the given transaction ID xid.

        This method should be called outside of a transaction
        (i.e. nothing may have executed since the last .commit()
        or .rollback()).
        Furthermore, it is an error to call .commit() or .rollback() within
        the TPC transaction. A ProgrammingError is raised, if the application
        calls .commit() or .rollback() during an active TPC transaction.
        """

        self._check_closed()
        if type(xid).__name__ != "xid":
            raise mariadb.ProgrammingError("argument 1 must be xid "
                                           "not %s", type(xid).__name__)
        stmt = "XA BEGIN '%s','%s',%s" % (xid[1], xid[2], xid[0])
        try:
            self._execute_command(stmt)
            self._read_response()
        except mariadb.Error:
            raise
        self.tpc_state = TPC_STATE.XID
        self._xid = xid

    def tpc_commit(self, xid=None):
        """
        Optional parameter:"
        xid: xid object which was created by .xid() method of connection class.

        When called with no arguments, .tpc_commit() commits a TPC transaction
        previously prepared with .tpc_prepare().

        If .tpc_commit() is called prior to .tpc_prepare(), a single phase
        commit is performed. A transaction manager may choose to do this if
        only a single resource is participating in the global transaction.
        When called with a transaction ID xid, the database commits the given
        transaction. If an invalid transaction ID is provided,
        a ProgrammingError will be raised.
        This form should be called outside of a transaction, and
        is intended for use in recovery."
        """

        self._check_closed()
        if not xid:
            xid = self._xid

        if self.tpc_state == TPC_STATE.NONE:
            raise mariadb.ProgrammingError("Transaction not started.")
        if xid is None and self.tpc_state != TPC_STATE.PREPARE:
            raise mariadb.ProgrammingError("Transaction is not prepared.")
        if xid and type(xid).__name__ != "xid":
            raise mariadb.ProgrammingError("argument 1 must be xid "
                                           "not %s" % type(xid).__name__)

        if self.tpc_state < TPC_STATE.PREPARE:
            stmt = "XA END '%s','%s',%s" % (xid[1], xid[2], xid[0])
            self._execute_command(stmt)
            try:
                self._read_response()
            except mariadb.Error:
                self._xid = None
                self.tpc_state = TPC_STATE.NONE
                raise

        stmt = "XA COMMIT '%s','%s',%s" % (xid[1], xid[2], xid[0])
        if self.tpc_state < TPC_STATE.PREPARE:
            stmt = stmt + " ONE PHASE"
        try:
            self._execute_command(stmt)
            self._read_response()
        except mariadb.Error:
            self._xid = None
            self.tpc_state = TPC_STATE.NONE
            raise

        # cleanup
        self._xid = None
        self.tpc_state = TPC_STATE.NONE

    def tpc_prepare(self):
        """
        Performs the first phase of a transaction started with .tpc_begin().
        A ProgrammingError will be raised if this method was called outside of
        a TPC transaction.

        After calling .tpc_prepare(), no statements can be executed until
        .tpc_commit() or .tpc_rollback() have been called.
        """

        self._check_closed()
        if self.tpc_state == TPC_STATE.NONE:
            raise mariadb.ProgrammingError("Transaction not started.")
        if self.tpc_state == TPC_STATE.PREPARE:
            raise mariadb.ProgrammingError("Transaction is already in "
                                           "prepared state.")

        xid = self._xid
        stmt = "XA END '%s','%s',%s" % (xid[1], xid[2], xid[0])
        try:
            self._execute_command(stmt)
            self._read_response()
        except mariadb.Error:
            self._xid = None
            self.tpc_state = TPC_STATE.NONE
            raise

        stmt = "XA PREPARE '%s','%s',%s" % (xid[1], xid[2], xid[0])
        try:
            self._execute_command(stmt)
            self._read_response()
        except mariadb.Error:
            self._xid = None
            self.tpc_state = TPC_STATE.NONE
            raise

        self.tpc_state = TPC_STATE.PREPARE

    def tpc_rollback(self, xid=None):
        """
        Parameter:
           xid: xid object which was created by .xid() method of connection
                class

        Performs the first phase of a transaction started with .tpc_begin().
        A ProgrammingError will be raised if this method outside of a TPC
        transaction.

        After calling .tpc_prepare(), no statements can be executed until
        .tpc_commit() or .tpc_rollback() have been called.
        """

        self._check_closed()
        if self.tpc_state == TPC_STATE.NONE:
            raise mariadb.ProgrammingError("Transaction not started.")
        if xid and type(xid).__name__ != "xid":
            raise mariadb.ProgrammingError("argument 1 must be xid "
                                           "not %s" % type(xid).__name__)

        if not xid:
            xid = self._xid

        if self.tpc_state < TPC_STATE.PREPARE:
            stmt = "XA END '%s','%s',%s" % (xid[1], xid[2], xid[0])
            self._execute_command(stmt)
            try:
                self._read_response()
            except mariadb.Error:
                self._xid = None
                self.tpc_state = TPC_STATE.NONE
                raise

        stmt = "XA ROLLBACK '%s','%s',%s" % (xid[1], xid[2], xid[0])
        try:
            self._execute_command(stmt)
            self._read_response()
        except mariadb.Error:
            self._xid = None
            self.tpc_state = TPC_STATE.NONE
            raise

        self.tpc_state = TPC_STATE.PREPARE

    def tpc_recover(self):
        """
        Returns a list of pending transaction IDs suitable for use with
        tpc_commit(xid) or .tpc_rollback(xid).
        """

        self._check_closed()
        cursor = self.cursor()
        cursor.execute("XA RECOVER")
        result = cursor.fetchall()
        del cursor
        return result

    @property
    def database(self):
        """Get default database for connection."""

        self._check_closed()
        return self._mariadb_get_info(INFO.SCHEMA)

    @database.setter
    def database(self, schema):
        """Set default database."""
        self._check_closed()

        try:
            self._execute_command("USE %s" % str(schema))
            self._read_response()
        except mariadb.Error:
            raise

    @property
    def user(self):
        """
        Returns the user name for the current connection or empty
        string if it can't be determined, e.g. when using socket
        authentication.
        """
        self._check_closed()

        return self._mariadb_get_info(INFO.USER)

    @property
    def character_set(self):
        """
        Client character set.

        For MariaDB Connector/Python it is always utf8mb4.
        """

        return _DEFAULT_CHARSET

    @property
    def client_capabilities(self):
        """Client capability flags."""

        self._check_closed()
        return self._mariadb_get_info(INFO.CLIENT_CAPABILITIES)

    @property
    def server_capabilities(self):
        """Server capability flags."""

        self._check_closed()
        return self._mariadb_get_info(INFO.SERVER_CAPABILITIES)

    @property
    def extended_server_capabilities(self):
        """
        Extended server capability flags (only for MariaDB
        database servers).
        """

        self._check_closed()
        return self._mariadb_get_info(INFO.EXTENDED_SERVER_CAPABILITIES)

    @property
    def server_port(self):
        """
        Database server TCP/IP port. This value will be 0 in case of a unix
        socket connection.
        """

        self._check_closed()
        return self._mariadb_get_info(INFO.PORT)

    @property
    def unix_socket(self):
        """Unix socket name."""

        self._check_closed()
        return self._mariadb_get_info(INFO.UNIX_SOCKET)

    @property
    def server_name(self):
        """Name or IP address of database server."""

        self._check_closed()
        return self._mariadb_get_info(INFO.HOST)

    @property
    def collation(self):
        """Client character set collation"""

        return _DEFAULT_COLLATION

    @property
    def server_info(self):
        """Server version in alphanumerical format (str)"""

        self._check_closed()
        return self._mariadb_get_info(INFO.SERVER_VERSION)

    @property
    def tls_cipher(self):
        """TLS cipher suite if a secure connection is used."""

        self._check_closed()
        return self._mariadb_get_info(INFO.SSL_CIPHER)

    @property
    def tls_version(self):
        """TLS protocol version if a secure connection is used."""

        self._check_closed()
        return self._mariadb_get_info(INFO.TLS_VERSION)

    @property
    def server_status(self):
        """
        Return server status flags
        """

        self._check_closed()
        return self._mariadb_get_info(INFO.SERVER_STATUS)

    @property
    def server_version(self):
        """
        Server version in numerical format.

        The form of the version number is
        VERSION_MAJOR * 10000 + VERSION_MINOR * 100 + VERSION_PATCH
        """

        self._check_closed()
        return self._mariadb_get_info(INFO.SERVER_VERSION_ID)

    @property
    def server_version_info(self):
        """
        Returns numeric version of connected database server in tuple format.
        """

        self._check_closed()
        version = self.server_version
        return (int(version / 10000),
                int((version % 10000) / 100),
                version % 100)

    @property
    def autocommit(self):
        """
        Toggles autocommit mode on or off for the current database connection.

        Autocommit mode only affects operations on transactional table types.
        Be aware that rollback() will not work, if autocommit mode was switched
        on.

        By default autocommit mode is set to False."
        """

        self._check_closed()
        return bool(self.server_status & STATUS.AUTOCOMMIT)

    @autocommit.setter
    def autocommit(self, mode):
        self._check_closed()
        if bool(mode) == self.autocommit:
            return
        try:
            self._execute_command("SET AUTOCOMMIT=%s" % int(mode))
            self._read_response()
        except mariadb.Error:
            raise

    @property
    def socket(self):
        """Returns the socket used for database connection"""

        fno = self._get_socket()
        if not self._socket:
            self._socket = socket.socket(fileno=fno)
        # in case of a possible reconnect, file descriptor has changed
        elif fno != self._socket.fileno():
            self._socket = socket.socket(fileno=fno)
        return self._socket

    @property
    def open(self):
        """
        Returns true if the connection is alive.

        A ping command will be send to the server for this purpose,
        which means this function might fail if there are still
        non processed pending result sets.
        """

        self._check_closed()
        try:
            self.ping()
        except mariadb.Error:
            return False
        return True

    # Aliases
    character_set_name = character_set

    @property
    def thread_id(self):
        """
        Alias for connection_id
        """

        self._check_closed()
        return self.connection_id
