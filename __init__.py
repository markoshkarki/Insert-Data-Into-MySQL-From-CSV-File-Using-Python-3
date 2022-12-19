import mysql.connector
from mysql.connector import errorcode

__author__ = "Markosh Karki"


try:
    connection = mysql.connector.connect(
        host='localhost', user='root', password='', database='')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version:", db_Info)
        cursor = connection.cursor()
        cursor.execute(
            "CREATE DATABASE employees DEFAULT CHARACTER SET 'utf8'")
        print('Database created successfully!')
        cursor.execute('USE employees')
        # use below commented code if you want to create database from MySQL workbench
        # first create a database in MySQL Workbench
        # cursor.execute('SELECT database();')
        # record = cursor.fetchone()
        # print("You're connected to database:", record)

except mysql.connector.Error as e:
    if e.errno == errorcode.ER_DB_CREATE_EXISTS:
        print('Database already exists!')
    else:
        print('Error while connecting to MySQL', e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed!")
