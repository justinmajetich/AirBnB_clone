"""MariaDB FIELD_FLAG Constants

These constants represent the various field flags. As an addition
to the DBAPI 2.0 standard (PEP-249) these flags are returned as
eighth element of the cursor description attribute.

Field flags are defined in module *mariadb.constants.FIELD_FLAG*
"""

# Source: mariadb_com.h (MariaDB Connector(C)

NOT_NULL = 1
PRIMARY_KEY = 2
UNIQUE_KEY = 4
MULTIPLE_KEY = 8
BLOB = 16
UNSIGNED = 32
ZEROFILL = 64
BINARY = 128
ENUM = 256
AUTO_INCREMENT = 512
TIMESTAMP = 1024
SET = 2048
NO_DEFAULT = 4096
ON_UPDATE_NOW = 8192
NUMERIC = 32768
PART_OF_KEY = 16384
GROUP = 32768
UNIQUE = 65536
