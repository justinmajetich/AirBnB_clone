
⋊> ~/a/AirBnB_clone_v2 on dennis ⨯ echo 'create State name="California"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
storage t ===  db
storage t ===  db
(hbnb)
 ====  new class instance created   start  ===
[State] (2bad95a0-2475-4cc1-a7b3-393f985fbb9c) {'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at
0x7f10559855b0>, 'id': '2bad95a0-2475-4cc1-a7b3-393f985fbb9c', 'created_at': datetime.datetime(2022, 9, 11, 22, 57, 27,
187501), 'updated_at': datetime.datetime(2022, 9, 11, 22, 57, 27, 187518), 'name': 'California'}
 ====  new class instance created  end =====
(hbnb)
⋊> ~/a/AirBnB_clone_v2 on dennis ⨯ echo 'all State' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
storage t ===  db
storage t ===  db
(hbnb)
 ====   all instances  start  ===
[State] (2bad95a0-2475-4cc1-a7b3-393f985fbb9c) {'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at
0x7f73ab2b15b0>, 'created_at': datetime.datetime(2022, 9, 11, 22, 57, 27), 'name': 'California', 'id':
'2bad95a0-2475-4cc1-a7b3-393f985fbb9c', 'updated_at': datetime.datetime(2022, 9, 11, 19, 57, 27)}
[State] (c1c77d47-5034-43df-97cc-d115d1e90ed8) {'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at
0x7f73ab2b1550>, 'created_at': datetime.datetime(2022, 9, 11, 22, 40, 38), 'name': 'California', 'id':
'c1c77d47-5034-43df-97cc-d115d1e90ed8', 'updated_at': datetime.datetime(2022, 9, 11, 19, 40, 38)}
 ====   all instances end =====
(hbnb)
⋊> ~/a/AirBnB_clone_v2 on dennis ⨯ echo 'SELECT * FROM states\G' | mysql -uhbnb_dev -p hbnb_dev_db               22:58:36
Enter password:
*************************** 1. row ***************************
        id: 2bad95a0-2475-4cc1-a7b3-393f985fbb9c
created_at: 2022-09-11 22:57:27
updated_at: 2022-09-11 19:57:27
      name: California
*************************** 2. row ***************************
        id: c1c77d47-5034-43df-97cc-d115d1e90ed8
created_at: 2022-09-11 22:40:38
updated_at: 2022-09-11 19:40:38
      name: California
⋊> ~/a/AirBnB_clone_v2 on dennis ⨯ echo 'create City state_id="c1c77d47-5034-43df-97cc-d115d1e90ed8" name="San_Francisco"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
storage t ===  db
storage t ===  db
(hbnb)
 ====  new class instance created   start  ===
[City] (fba5934a-fba2-457b-a1e2-350bed7739d1) {'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at
0x7fa4d8a005b0>, 'id': 'fba5934a-fba2-457b-a1e2-350bed7739d1', 'created_at': datetime.datetime(2022, 9, 11, 22, 59, 56,
339122), 'updated_at': datetime.datetime(2022, 9, 11, 22, 59, 56, 339140), 'state_id':
'c1c77d47-5034-43df-97cc-d115d1e90ed8', 'name': 'San Francisco'}
 ====  new class instance created  end =====
(hbnb)
⋊> ~/a/AirBnB_clone_v2 on dennis ⨯ echo 'all City' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
storage t ===  db
storage t ===  db
(hbnb)
 ====   all instances  start  ===
[City] (fba5934a-fba2-457b-a1e2-350bed7739d1) {'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at
0x7f7d38dad790>, 'updated_at': datetime.datetime(2022, 9, 11, 19, 59, 56), 'id': 'fba5934a-fba2-457b-a1e2-350bed7739d1',
'name': 'San Francisco', 'created_at': datetime.datetime(2022, 9, 11, 22, 59, 56), 'state_id':
'c1c77d47-5034-43df-97cc-d115d1e90ed8'}
 ====   all instances end =====
(hbnb)
⋊> ~/a/AirBnB_clone_v2 on dennis ⨯ echo 'create City state_id="c1c77d47-5034-43df-97cc-d115d1e90ed8" name="San_Jose"' | H
BNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
storage t ===  db
storage t ===  db
(hbnb)
 ====  new class instance created   start  ===
[City] (afdb9f6e-b4dc-41b2-8e93-11a798bdb44f) {'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at
0x7f7f2adb75b0>, 'id': 'afdb9f6e-b4dc-41b2-8e93-11a798bdb44f', 'created_at': datetime.datetime(2022, 9, 11, 23, 2, 5,
241192), 'updated_at': datetime.datetime(2022, 9, 11, 23, 2, 5, 241210), 'state_id':
'c1c77d47-5034-43df-97cc-d115d1e90ed8', 'name': 'San Jose'}
 ====  new class instance created  end =====
(hbnb)
⋊> ~/a/AirBnB_clone_v2 on dennis ⨯ echo 'SELECT * FROM cities\G' | mysql -uhbnb_dev -p hbnb_dev_db               23:02:19
Enter password:
*************************** 1. row ***************************
        id: afdb9f6e-b4dc-41b2-8e93-11a798bdb44f
created_at: 2022-09-11 23:02:05
updated_at: 2022-09-11 20:02:05
  state_id: c1c77d47-5034-43df-97cc-d115d1e90ed8
      name: San Jose
*************************** 2. row ***************************
        id: fba5934a-fba2-457b-a1e2-350bed7739d1
created_at: 2022-09-11 22:59:56
updated_at: 2022-09-11 19:59:56
  state_id: c1c77d47-5034-43df-97cc-d115d1e90ed8
      name: San Francisco
⋊> ~/a/AirBnB_clone_v2 on dennis ⨯       
