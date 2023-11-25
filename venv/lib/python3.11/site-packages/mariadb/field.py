from mariadb.constants import FIELD_TYPE, FIELD_FLAG

field_types = {FIELD_TYPE.DECIMAL: "DECIMAL",
               FIELD_TYPE.TINY:  "TINY",
               FIELD_TYPE.SHORT: "SHORT",
               FIELD_TYPE.LONG: "LONG",
               FIELD_TYPE.FLOAT: "FLOAT",
               FIELD_TYPE.DOUBLE: "DOUBLE",
               FIELD_TYPE.NULL: "NULL",
               FIELD_TYPE.TIMESTAMP: "TIMESTAMP",
               FIELD_TYPE.LONGLONG: "LONGLONG",
               FIELD_TYPE.INT24: "INT24",
               FIELD_TYPE.DATE: "DATE",
               FIELD_TYPE.TIME: "TIME",
               FIELD_TYPE.DATETIME: "DATETIME",
               FIELD_TYPE.YEAR: "YEAR",
               FIELD_TYPE.NEWDATE: "NEWDATE",
               FIELD_TYPE.VARCHAR: "VARCHAR",
               FIELD_TYPE.BIT: "BIT",
               FIELD_TYPE.JSON: "JSON",
               FIELD_TYPE.NEWDECIMAL: "NEWDECIMAL",
               FIELD_TYPE.ENUM: "ENUM",
               FIELD_TYPE.SET: "SET",
               FIELD_TYPE.TINY_BLOB: "TINY_BLOB",
               FIELD_TYPE.MEDIUM_BLOB: "MEDIUM_BLOB",
               FIELD_TYPE.LONG_BLOB: "LONG_BLOB",
               FIELD_TYPE.BLOB: "BLOB",
               FIELD_TYPE.VAR_STRING: "VAR_STRING",
               FIELD_TYPE.STRING: "STRING",
               FIELD_TYPE.GEOMETRY: "GEOMETRY"}

field_flags = {FIELD_FLAG.NOT_NULL: "NOT_NULL",
               FIELD_FLAG.PRIMARY_KEY: "PRIMARY_KEY",
               FIELD_FLAG.UNIQUE_KEY: "UNIQUE_KEY",
               FIELD_FLAG.MULTIPLE_KEY: "PART_KEY",
               FIELD_FLAG.BLOB: "BLOB",
               FIELD_FLAG.UNSIGNED: "UNSIGNED",
               FIELD_FLAG.ZEROFILL: "ZEROFILL",
               FIELD_FLAG.BINARY: "BINARY",
               FIELD_FLAG.ENUM: "NUMERIC",
               FIELD_FLAG.AUTO_INCREMENT: "AUTO_INCREMENT",
               FIELD_FLAG.TIMESTAMP: "TIMESTAMP",
               FIELD_FLAG.SET: "SET",
               FIELD_FLAG.NO_DEFAULT: "NO_DEFAULT",
               FIELD_FLAG.ON_UPDATE_NOW: "UPDATE_TIMESTAMP",
               FIELD_FLAG.NUMERIC: "NUMERIC"}


class fieldinfo():

    def type(self, description):
        if description[1] in field_types:
            return field_types[description[1]]
        return None

    def flag(self, description):
        flags = [field_flags[f] for f in field_flags.keys()
                 if description[7] & f]
        return " | ".join(flags)
