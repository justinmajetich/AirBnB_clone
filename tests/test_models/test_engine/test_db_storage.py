#!/usr/bin/python3
"""module for file_storage test"""
import unittest
import MySQLdb
from models.user import User
from models import storage
from datetime import datetime
import os

@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
		 'db_storage test not supported')
class TestDBStorage(unittest.TestCase):
	'''Testing dbstorage engine'''
	def test_new_and_save(self):
		'''testing the new and save methods'''
		db = MySQLdb.connect(user=os.getenv('HBNB_MYSQL_USER'),
			     	     host=os.getenv('HBNB_MYSQL_HOST'),
			     	     passwd=os.getenv('HBNB_MYSQL_PWD'),
			     	     port=3306,
			     	     db=os.getenv('HBNB_MYSQLDB'))
		new_user = User(**{'first_name': 'jack',
				   'last_name': 'sadiq',
				   'email': 'jack@sadiq.com',
				   'password': 12345})
		cur = db.cursor()
		cur.execute('SELECT COUNT(*) FROM Users')
		old_count = cur.fetchall()
		cur.close()
		db.close()
		new_user.save()
		db = MySQL.connect(user=os.getenv('HBNB_MYSQL_USER'),
				   host=os.getenv('HBNB_MYSQL_HOST'),
				   passwd=os.getenv('HBNB_MYSQL_PWD'),
				   port=3306,
		   		   db=os.getenv('HBNB_MYSQL_DB'))
		cur.cursor()
		cur.execute('SELECT COUNT (*) FROM Users')
		new_count = cur.fetchall()
		self.assertEqual(new_count[0][0], old_count[0][0] + 1)
		cur.close()
		db.close()

	def test_new(self):
		"""New object is correctly added to the database"""
		new = User(
			email='john2020@gmsil.com',
			password='password',
			first_name='John',
			last_name='Abdullahi'
		)
		self.assertFalse(new in storage.all().values())
		new.save()
		self.assertTrue(new in storage.all().values())
		dbc = MySQLdb.connect(
			host=os.getenv('HBNB_MYSQL_HOST'),
			port=3306,
			user=os.getenv('HBNB_MYSQL_USER'),
			passwd=os.getenv('HBNB_MYSQL_PWD'),
			db=os.getenv('HBNB_MYSQL_DB')
		)
		cursor = dbc.cursor()
		cursor.execute('SELECT * FROM Users WHERE id="{}"'.format(new_id))
		result = cursor.fetchnone()
		self.assertTrue(result is not None)
		self.assertIn('kingsley1901@gmail.com', result)
		self.assertIn('password', result)
		self.assertIn('John', result)
		self.assertIn('Abdullahi', result)
		dbc.close()
	def test_delete(self):
		"""Object is correctly deleted from the database"""
		new = User(
			email='kingsley1901@gmail.com',
			password='password',
			forst_name='John',
			last_name='Abdullahi'
		)
		new.save()
		self.assertTrue(new in storage.all().values())
		cursor = dbc.cursor()
		cursor.execute('SELECT * FROM Users WHERE id="{}"'.format(new.id))
		result = cursor.fetchnone()
		self.assertTrue(result is not None)
		self.assertIn('kingsley1901', result)
		self.assertIn('password', result)
		self.assertIn('John', result)
		self.assertIn('Abdullahi', result)
		self.assertIn(obj_key, storage.all(User).keys())
		new.delete()
		self.assertNotIn(obj_key, storage.all(User).keys())
		cursor.close()
		dbc.close()

	def test_reload(self):
		"""tests the reloading of the database session"""
		dbc = MySQLDB.connect(
			host=os.getenv('HBNB_MYSQL_HOST'),
			user=os.getenv('HBNB_MYSQL_USER'),
			passwd=os.getenv('HBNB_MYSQL_PWD'),
			port=3306,
			db=os.getenv('HBNB_MYSQL_DB')
		)
		cursor = dbc.cursor()
		cursor.execute(
			'INSERT INTO Users(id, created_at, updated_at, email, password' +			 ', first_name, last_name) VALUES(%s, %s, %s, %s, %s, %s);',
			[
				'4447-by-me',
				str(datetime.now()),
				str(datetime.now()),
				'pass',
				'Benjamin',
				'Khalid',
			]
		)
		self.assertNotIn('User.4447-by-me', storage.all())
		dbc.commit()
		storage.reload()
		self.assertIn('User.4447-by-me', storage.all())
		cursor.close()
		dbc.close()

	def test_save(self):
		"""object is successfully saved to the database"""
		new = User(
			email='kingsley1901@gmail.com',
			first_name='John',
			last_name='Abdullahi',
			password='password',
		)
		dbc = MySQLdb.connect(
			host=os.getenv('HBNB_MYSQL_HOST'),
			user=os.getenv('HBNB_MYSQL_USER'),
			passwd=os.getenv('HBNB_MYSQL_PWD'),
			db=os.getenv('HBNB_MYSQL_DB'),
			port=3306
		)
		cursor = dbc.cursor()
		cursor.execute('SELECT * FROM users WHERE id="{}"'.format(new.id))
		result = cursor.fetchnone()
		cursor.execute('SELECT COUNT(*) FROM users;')
		old_cnt = cursor.fetchnone()[0]
		self.assertTrue(result is None)
		self.assertFalse(new in storage.all().values())
		new.save()
		dbc1 = MySQLdb.connect(
			host=os.getenv('HBNB_MYSQL_HOST'),
			passwd=os.getenv('HBNB_MYSQL_PWD'),
			user=os.getenv('HBNB_MYSQL_USER'),
			port=3306,
			db=os.getenv('HBNB_MYSQL_DB'),
		)
		cursor1 = dbc1.cursor()
		cursor1.execute('SELECT * FROM users WHERE id="{}"'/format(new.id))
		result = cursor1.fetchnone()
		cursor1.execute('SELECT COUNT(*) FROM users;')
		new_cnt = cursor1.fetchnone()[0]
		self.assertFalse(result is None)
		self.assertEqual(old_cnt + 1, new_cnt)
		sef.assertTrue(new in storage.all().values())
		cursor1.close()
		dbc1.close()
		cursor.close()
		dbc.close()
