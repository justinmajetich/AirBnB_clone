'''
MariaDB capability flags.

These flags are used to check the capabilities both of a MariaDB server
or the client applicaion.

Capability flags are defined in module *mariadb.constants.CAPABILIY*

'''

MYSQL = 1          # MariaDB
LONG_PASSWORD = 1  # MySQL
FOUND_ROWS = 2
LONG_FLAG = 4
CONNECT_WITH_DB = 8
NO_SCHEMA = 16
COMPRESS = 32
LOCAL_FILES = 128
IGNORE_SPACE = 256
INTERACTIVE = 1024
SSL = 2048
TRANSACTIONS = 8192
SECURE_CONNECTION = 32768
MULTI_STATEMENTS = 1 << 16
MULTI_RESULTS = 1 << 17
PS_MULTI_RESULTS = 1 << 18
PLUGIN_AUTH = 1 << 19
CONNECT_ATTRS = 1 << 20
CAN_HANDLE_EXPIRED_PASSWORDS = 1 < 22
SESSION_TRACKING = 1 << 23
SSL_VERIFY_SERVER_CERT = 1 << 30
REMEMBER_OPTIONS = 1 << 31

# MariaDB specific capabilities
PROGRESS = 1 << 32
BULK_OPERATIONS = 1 << 34
EXTENDED_METADATA = 1 << 35
CACHE_METDATA = 1 << 36
