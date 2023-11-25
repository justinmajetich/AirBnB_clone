'''
MariaDB Connector/Python module enables python programs to access MariaDB and
MySQL databases, using an API which is compliant with the Python DB API 2.0
(PEP-249).
'''
import mariadb
from ._mariadb import (
    DataError,
    DatabaseError,
    Error,
    IntegrityError,
    InterfaceError,
    InternalError,
    NotSupportedError,
    OperationalError,
    PoolError,
    ProgrammingError,
    Warning,
    mariadbapi_version,
)

from .field import fieldinfo
from mariadb.dbapi20 import *   # noqa: F401,F403
from mariadb.connectionpool import *   # noqa: F401,F403
from mariadb.cursors import Cursor
from mariadb.release_info import __version__ as __version__
from mariadb.release_info import __version_info__ as __version_info__
from mariadb.release_info import __author__ as __author__
from mariadb.connections import Connection
# disable for now, until tests are in place
# from mariadb.pooling import *

_POOLS = _CONNECTION_POOLS = {}

__all__ = ["DataError", "DatabaseError", "Error", "IntegrityError",
           "InterfaceError", "InternalError", "NotSupportedError",
           "OperationalError", "PoolError", "ProgrammingError",
           "Warning", "Connection", "__version__", "__version_info__",
           "__author__", "Cursor", "fieldinfo"]


def connect(*args, connectionclass=mariadb.connections.Connection, **kwargs):
    """
    Creates a MariaDB Connection object.

    By default the standard connectionclass mariadb.connections.Connection
    will be created.

    Parameter connectionclass specifies a subclass of
    mariadb.Connection object. If not specified default will be used.
    This optional parameter was added in version 1.1.0.

    Connection parameters are provided as a set of keyword arguments:
        - host:
            The host name or IP address of the database server.
            If MariaDB Connector/Python was built with MariaDB Connector/C 3.3
            it is also possible to provide a comma separated list of hosts for
            simple fail over in case of one or more hosts are not available.
        - user, username:
            The username used to authenticate with the database server
        - password, passwd:
            The password of the given user
        - database, db:
            database (schema) name to use when connecting with the database
            server
        - unix_socket:
            The location of the unix socket file to use instead of using an IP
            port to connect. If socket authentication is enabled, this can also
            be used in place of a password.
        - port:
            port number of the database server. If not specified the default
            value of 3306 will be used.
        - connect_timeout:
            connect timeout in seconds
        - read_timeout:
            read timeout in seconds
        - write_timeout:
            write timeout in seconds
        - local_infile:
            Enables or disables the use of LOAD DATA LOCAL INFILE statements.
        - compress= False:
            Uses the compressed protocol for client server communication. If
            the server doesn't support compressed protocol, the default
            protocol will be used.
        - init_command:
            Command(s) which will be executed when connecting and reconnecting
            to the database server
        - default_file:
            Read options from the specified option file. If the file is an
            empty string, default configuration file(s) will be used
        - default_group:
            Read options from the specified group
        - plugin_dir:
            Directory which contains MariaDB client plugins.
        - reconnect:
            Enables or disables automatic reconnect. Available since
            version 1.1.4
        - ssl_key:
            Defines a path to a private key file to use for TLS. This option
            requires that you use the absolute path, not a relative path. The
            specified key must be in PEM format
        - ssl_cert:
            Defines a path to the X509 certificate file to use for TLS.
            This option requires that you use the absolute path, not a relative
            path. The X609 certificate must be in PEM format.
        - ssl_ca:
            Defines a path to a PEM file that should contain one or more X509
            certificates for trusted Certificate Authorities (CAs) to use for
            TLS.  This option requires that you use the absolute path, not a
            relative path.
        - ssl_capath:
            Defines a path to a directory that contains one or more PEM files
            that contains one X509 certificate for a trusted Certificate
            Authority (CA)
        - ssl_cipher:
            Defines a list of permitted cipher suites to use for TLS
        - ssl_crlpath:
            Defines a path to a PEM file that should contain one or more
            revoked X509 certificates to use for TLS. This option requires
            that you use the absolute path, not a relative path.
        - ssl_verify_cert:
            Enables server certificate verification.
        - ssl:
            The connection must use TLS security or it will fail.
        - tls_version:
            A comma-separated list (without whitespaces) of TLS versions.
            Valid versions are TLSv1.0, TLSv1.1,TLSv1.2 and TLSv1.3.
            Added in version 1.1.7.
        - autocommit=False:
            Specifies the autocommit settings.
            True will enable autocommit, False will disable it (default).
        - converter:
            Specifies a conversion dictionary, where keys are FIELD_TYPE
            values and values are conversion functions

    """
    if kwargs:
        if "pool_name" in kwargs:
            if not kwargs["pool_name"] in mariadb._CONNECTION_POOLS:
                pool = mariadb.ConnectionPool(**kwargs)
            else:
                pool = mariadb._CONNECTION_POOLS[kwargs["pool_name"]]
            c = pool.get_connection()
            return c

    connection = connectionclass(*args, **kwargs)
    if not isinstance(connection, mariadb.connections.Connection):
        raise mariadb.ProgrammingError("%s is not an instance of "
                                       "mariadb.Connection" % connection)
    return connection


client_version_info = tuple(int(x, 10) for x in mariadbapi_version.split('.'))
client_version = client_version_info[0] * 10000 +\
    client_version_info[1] * 1000 + client_version_info[2]
