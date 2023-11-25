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
import datetime
from numbers import Number
from mariadb.constants import CURSOR, STATUS, CAPABILITY, INDICATOR
from typing import Sequence

PARAMSTYLE_QMARK = 1
PARAMSTYLE_FORMAT = 2
PARAMSTYLE_PYFORMAT = 3

ROWS_ALL = -1

RESULT_TUPLE = 0
RESULT_NAMEDTUPLE = 1
RESULT_DICTIONARY = 2

# Command types
SQL_NONE = 0,
SQL_INSERT = 1
SQL_UPDATE = 2
SQL_REPLACE = 3
SQL_DELETE = 4
SQL_CALL = 5
SQL_DO = 6
SQL_SELECT = 7
SQL_OTHER = 255

ROWS_EOF = -1


class Cursor(mariadb._mariadb.cursor):
    """
    MariaDB Connector/Python Cursor Object
    """

    def check_closed(self):
        if self.closed:
            self._connection._check_closed()
            raise mariadb.ProgrammingError("Cursor is closed")

    def __init__(self, connection, **kwargs):
        """
        initialization
        """
        self._bulk = False
        self._dictionary = False
        self._named_tuple = False
        self._connection = connection
        self._resulttype = RESULT_TUPLE
        self._description = None
        self._transformed_statement = None
        self._prepared = False
        self._prev_stmt = None
        self._force_binary = None
        self._rowcount = 0
        self.buffered = True
        self._parseinfo = None
        self._data = None

        if not connection:
            raise mariadb.ProgrammingError("Invalid or no connection provided")

        # parse keywords
        if kwargs:
            rtype = kwargs.pop("named_tuple", False)
            if rtype:
                self._resulttype = RESULT_NAMEDTUPLE
            else:
                rtype = kwargs.pop("dictionary", False)
                if rtype:
                    self._resulttype = RESULT_DICTIONARY
            buffered = kwargs.pop("buffered", True)
            self.buffered = buffered
            self._prepared = kwargs.pop("prepared", False)
            self._force_binary = kwargs.pop("binary", False)
            self._cursor_type = kwargs.pop("cursor_type", 0)

        # call initialization of main class
        super().__init__(connection, **kwargs)

    def _substitute_parameters(self):
        """
        Internal use only.

        When running in text protocol, this method will replace placeholders
        by supplied values.

        For values which aren't numbers, strings or bytes string representation
        will be used.
        """

        new_stmt = self.statement.encode("utf8")
        replace_diff = 0
        if self._paramlist:
            for i in range(0, len(self._paramlist)):
                extra_bytes = 0
                if self._paramstyle == PARAMSTYLE_PYFORMAT:
                    val = self._data[self._keys[i]]
                else:
                    val = self._data[i]
                if val is None:
                    replace = "NULL"
                else:
                    if isinstance(val, INDICATOR.MrdbIndicator):
                        if val == INDICATOR.NULL:
                            replace = "NULL"
                        if val == INDICATOR.DEFAULT:
                            replace = "DEFAULT"
                    elif isinstance(val, Number):
                        replace = val.__str__()
                    else:
                        if isinstance(val, (bytes, bytearray)):
                            replace = "\"%s\"" % self.connection.escape_string(
                                val.decode(encoding='latin1'))
                        else:
                            replace = "\"%s\"" % self.connection.escape_string(
                                val.__str__())
                            extra_bytes = len(replace.encode("utf-8")) -\
                                len(replace)
                ofs = self._paramlist[i] + replace_diff

                new_stmt = new_stmt[:ofs] + replace.__str__().encode("utf8") +\
                    new_stmt[ofs+1:]
                replace_diff += len(replace) - 1 + extra_bytes
        return new_stmt

    def _check_execute_params(self):
        # check data format
        if self._paramstyle in (PARAMSTYLE_QMARK, PARAMSTYLE_FORMAT):
            if not isinstance(self._data, (tuple, list)):
                raise mariadb.ProgrammingError("Data argument must be "
                                               "Tuple or List")

        if self._paramstyle == PARAMSTYLE_PYFORMAT:
            if not isinstance(self._data, dict):
                raise mariadb.ProgrammingError("Data argument must be "
                                               "Dictionary")
            for i in range(0, len(self._keys)):
                if self._keys[i] not in self._data:
                    raise mariadb.ProgrammingError("Dictionary doesn't contain"
                                                   " key '%s'" % self._keys[i])
        else:
            # check if number of place holders matches the number of
            # supplied elements in data tuple
            if self._paramlist and (
               (not self._data and len(self._paramlist) > 0) or
               (len(self._data) != len(self._paramlist))):
                raise mariadb.ProgrammingError(
                    "statement (%s) doesn't match the number of data elements"
                    " (%s)." % (len(self._paramlist), len(self._data)))

    def callproc(self, sp: str, data: Sequence = ()):
        """
        Executes a stored procedure sp. The data sequence must contain an
        entry for each parameter the procedure expects.

        Input/Output or Output parameters have to be retrieved by .fetch
        methods, the .sp_outparams attribute indicates if the result set
        contains output parameters.

        Arguments:
            - sp: Name of stored procedure.
            - data: Optional sequence containing data for placeholder
                    substitution.
        """

        self.check_closed()

        # create statement
        params = ""
        if data and len(data):
            params = ("?," * len(data))[:-1]
        statement = "CALL %s(%s)" % (sp, params)
        self._rowcount = 0
        self.execute(statement, data)

    def _parse_execute(self, statement: str, data=(), is_bulk=False):
        """
        For internal use

        Parses SQL statement and checks parameters.
        """

        if not statement:
            raise mariadb.ProgrammingError("empty statement")

        # parse statement
        if self.statement != statement or is_bulk and not self._bulk:
            super()._parse(statement)
            self._prev_stmt = statement
            self._reprepare = True
        else:
            self._reprepare = False

        self._transformed_statement = self.statement

        if self._cursor_type == CURSOR.READ_ONLY:
            self._text = False

        self._data = data

        self._check_execute_params()

    def nextset(self):
        """
        Will make the cursor skip to the next available result set,
        discarding any remaining rows from the current set.
        """

        self.check_closed()
        return super()._nextset()

    def execute(self, statement: str, data: Sequence = (), buffered=None):
        """
        Prepare and execute a SQL statement.

        Parameters may be provided as sequence or mapping and will be bound
        to variables in the operation. Variables are specified as question
        marks (paramstyle ='qmark'), however for compatibility reasons MariaDB
        Connector/Python also supports the 'format' and 'pyformat' paramstyles
        with the restriction, that different paramstyles can't be mixed within
        a statement.

        A reference to the operation will be retained by the cursor.
        If the cursor was created with attribute prepared =True the statement
        string for following execute operations will be ignored.
        This is most effective for algorithms where the same operation is used,
        but different parameters are bound to it (many times).

        By default execute() method generates an buffered result unless the
        optional parameter buffered was set to False or the cursor was
        generated as an unbuffered cursor.
        """

        self.check_closed()

        self.connection._last_executed_statement = statement

        # Parse statement
        do_parse = True
        self._rowcount = 0

        if buffered is not None:
            self.buffered = buffered

        # clear pending result sets
        if self.field_count:
            self._clear_result()

        # if we have a prepared cursor, we have to set statement
        # to previous statement and don't need to parse
        if self._prepared and self.statement:
            statement = self.statement
            do_parse = False

        # parse statement and check param style
        if do_parse:
            self._parse_execute(statement, (data))

        self._description = None

        # CONPY-218: Allow None as replacement for empty tuple
        data = data or ()

        if len(data):
            self._data = data
        else:
            self._data = None
            # If statement doesn't contain parameters we force to run in text
            # mode, unless a server side cursor or stored procedure will be
            # executed.
            if self._command != SQL_CALL and self._cursor_type == 0:
                self._text = True

        if self._force_binary:
            self._text = False

        # if one of the provided parameters has byte or datetime value,
        # we don't use text protocol
        if data and self._check_text_types() == True:
            self._text = False

        if self._text:
            # in text mode we need to substitute parameters
            # and store transformed statement
            if (self.paramcount > 0):
                self._transformed_statement = self._substitute_parameters()
            else:
                self._transformed_statement = self.statement

            self._execute_text(self._transformed_statement)
            self._readresponse()
        else:
            self._data = data
            self._execute_binary()

        self._initresult()
        self._bulk = 0

    def executemany(self, statement, parameters):
        """
        Prepare a database operation (INSERT,UPDATE,REPLACE or DELETE
        statement) and execute it against all parameter found in sequence.

        Exactly behaves like .execute() but accepts a list of tuples, where
        each tuple represents data of a row within a table.
        .executemany() only supports DML (insert, update, delete) statements.

        If the SQL statement contains a RETURNING clause, executemany()
        returns a result set containing the values for columns listed in the
        RETURNING clause.
        """
        self.check_closed()

        if not parameters or not len(parameters):
            raise mariadb.ProgrammingError("No data provided")

        self.connection._last_executed_statement = statement

        # clear pending results
        if self.field_count:
            self._clear_result()

        # If the server doesn't support bulk operations, we need to emulate
        # by looping
        # TODO: insert/replace statements are not optimized yet
        #       rowcount updating
        if not (self.connection.extended_server_capabilities &
                (CAPABILITY.BULK_OPERATIONS >> 32)):
            count = 0
            for row in parameters:
                self.execute(statement, row)
                count += self.rowcount
            self._rowcount = count
        else:
            # parse statement
            self._parse_execute(statement, parameters[0], is_bulk=True)
            self._data = parameters
            self.is_text = False
            self._rowcount = 0
            self._execute_bulk()
            self._bulk = 1

    def _fetch_row(self):
        """
        Internal use only

        fetches row and converts values, if connection has a converter.
        """
        self.check_closed()

        # if there is no result set, PEP-249 requires to raise an
        # exception
        if not self.field_count:
            raise mariadb.ProgrammingError("Cursor doesn't have a result set")
        return super().fetchone()

    def close(self):
        """
        Closes the cursor.

        If the cursor has pending or unread results, .close() will cancel them
        so that further operations using the same connection can be executed.

        The cursor will be unusable from this point forward; an Error
        (or subclass) exception will be raised if any operation is attempted
        with the cursor."
        """

        # CONPY-231: fix memory leak
        if self._data:
            del self._data

        if not self.connection._closed:
            super().close()

    def fetchone(self):
        """
        Fetch the next row of a query result set, returning a single sequence,
        or None if no more data is available.

        An exception will be raised if the previous call to execute() didn't
        produce a result set or execute() wasn't called before.
        """
        self.check_closed()

        row = self._fetch_row()
        return row

    def fetchmany(self, size: int = 0):
        """
        Fetch the next set of rows of a query result, returning a sequence
        of sequences (e.g. a list of tuples). An empty sequence is returned
        when no more rows are available.

        The number of rows to fetch per call is specified by the parameter.
        If it is not given, the cursor's arraysize determines the number
        of rows to be fetched. The method should try to fetch as many rows
        as indicated by the size parameter.
        If this is not possible due to the specified number of rows not being
        available, fewer rows may be returned.

        An exception will be raised if the previous call to execute() didn't
        produce a result set or execute() wasn't called before.
        """
        self.check_closed()

        if size == 0:
            size = self.arraysize

        return super().fetchrows(size)

    def fetchall(self):
        """
        Fetch all remaining rows of a query result, returning them as a
        sequence of sequences (e.g. a list of tuples).

        An exception will be raised if the previous call to execute() didn't
        produce a result set or execute() wasn't called before.
        """
        self.check_closed()
        return super().fetchrows(ROWS_EOF)

    def __iter__(self):
        return iter(self.fetchone, None)

    def scroll(self, value: int, mode="relative"):
        """
        Scroll the cursor in the result set to a new position according to
        mode.

        If mode is "relative" (default), value is taken as offset to the
        current position in the result set, if set to absolute, value states
        an absolute target position.
        """

        if self.field_count == 0:
            raise mariadb.ProgrammingError("Cursor doesn't have a result set")

        if not self.buffered:
            raise mariadb.ProgrammingError("This method is available only "
                                           "for cursors with a buffered "
                                           "result set.")

        if mode != "absolute" and mode != "relative":
            raise mariadb.ProgrammingError("Invalid or unknown scroll "
                                           "mode specified.")

        if value == 0 and mode != "absolute":
            raise mariadb.ProgrammingError("Invalid position value 0.")

        if mode == "relative":
            if self.rownumber + value < 0 or \
               self.rownumber + value > self.rowcount:
                raise mariadb.ProgrammingError("Position value "
                                               "is out of range.")
            new_pos = self.rownumber + value
        else:
            if value < 0 or value >= self.rowcount:
                raise mariadb.ProgrammingError("Position value "
                                               "is out of range.")
            new_pos = value

        self._seek(new_pos)
        self._rownumber = new_pos

    def setinputsizes(self, size: int):
        """
        Required by PEP-249. Does nothing in MariaDB Connector/Python
        """

        return

    def setoutputsize(self, size: int):
        """
        Required by PEP-249. Does nothing in MariaDB Connector/Python
        """

        return

    def __enter__(self):
        """Returns a copy of the cursor."""

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Closes cursor."""
        self.close()

    @property
    def rowcount(self):
        """
        This read-only attribute specifies the number of rows that the last\
        execute*() produced (for DQL statements like SELECT) or affected
        (for DML statements like UPDATE or INSERT).
        The return value is -1 in case no .execute*() has been performed
        on the cursor or the rowcount of the last operation  cannot be
        determined by the interface.
        """

        # Even if PEP-249 permits operations on a closed cursor, we don't
        # raise an exception if the cursor or the underlying connection
        # was closed (See CONPY-269), instead we will return -1
        try:
            self.check_closed()
        except mariadb.ProgrammingError:
            return -1

        if self._rowcount > 0:
            return self._rowcount
        return super().rowcount

    @property
    def sp_outparams(self):
        """
        Indicates if the current result set contains in out or out parameter
        from a previous executed stored procedure
        """
        self.check_closed()

        return bool(self.connection.server_status & STATUS.PS_OUT_PARAMS)

    @property
    def lastrowid(self):
        """
        Returns the ID generated by a query on a table with a column having
        the AUTO_INCREMENT attribute or the value for the last usage of
        LAST_INSERT_ID().

        If the last query wasn't an INSERT or UPDATE
        statement or if the modified table does not have a column with the
        AUTO_INCREMENT attribute and LAST_INSERT_ID was not used, the returned
        value will be zero
        """
        self.check_closed()

        id = self.insert_id
        if id > 0:
            return id
        return None

    @property
    def connection(self):
        """
        Read-Only attribute which returns the reference to the connection
        object on which the cursor was created.
        """
        self.check_closed()

        return self._connection
