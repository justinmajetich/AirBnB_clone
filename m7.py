#!/usr/bin/python3
"""Doc
"""
import MySQLdb
import sys
import uuid
from models import storage
from models.state import State


def add_states(number=1):
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()

    for i in range(number):
        cur.execute("INSERT INTO `states` (id, created_at, updated_at, name) VALUES ('{}','2016-03-25 19:42:40','2016-03-25 19:42:40','state{}');".format(str(uuid.uuid4()), i))

    conn.commit()
    cur.close()
    conn.close()


def wrapper_all_type(m_class):
    res = {}
    try:
        res = storage.all(m_class)
    except:
        res = {}
    if res is None or len(res.keys()) == 0:
        try:
            res = storage.all(m_class.__name__)
        except:
            res = {}
    return res
        

print(len(wrapper_all_type(State)))

# Initial number of states
add_states(3)

storage.close()
print(len(wrapper_all_type(State)))

# Add new states
add_states(2)

storage.close()
print(len(wrapper_all_type(State)))
