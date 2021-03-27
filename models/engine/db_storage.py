 #!/usr/bin/env python3
 from sqlalchemy import create_engine

 class DBStorage():
     __engine = None
     __session = None
     def __init__(self):
         self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        "hbnb_dev", "hbnb_dev_pwd", "hbnb_dev_db"), pool_pre_ping=True)
