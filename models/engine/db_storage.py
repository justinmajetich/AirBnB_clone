
class DBStorage:
    """Database storage engine.
    Private class attributes:
        __engine: set to None.
        __session: set to None.
    """

    __engine = None
    __session = None


    """Public instance methods:
        __init__(self):
        all(self, cls=None):
        new(self, obj):
        save(self):
        delete(self, obj=None):
        reload(self):
    """

    def __init__(self):
        """Initialize new engine instance
        Engine must be linked to:
         MySQL database, and
         user created before
         (hbnb_dev and hbnb_dev_db):
        """
        self.__engine = create_engine("mysql".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
