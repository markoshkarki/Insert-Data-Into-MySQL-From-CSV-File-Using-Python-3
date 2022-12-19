import mysql.connector
from mysql.connector import errorcode

try:
    connection = mysql.connector.connect(
        host='localhost', user='root', password='', database='employees')

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version:", db_Info)
        cursor = connection.cursor()
        cursor.execute('SELECT database();')
        record = cursor.fetchone()
        print("You're connected to database:", record)
        cursor.execute('DROP TABLE IF EXISTS employees_data')
        print('Existing table dropped to create new table!')

    mySql_Create_Table_Query = "CREATE TABLE employees_data(first_name varchar(255),last_name varchar(255),company_name varchar(255),address varchar(255),city varchar(255),country varchar(255),state varchar(255),zip varchar(255),phone1 varchar(255),phone2 varchar(255),email varchar(255),web varchar(255))"

    result = cursor.execute(mySql_Create_Table_Query)
    print("employees table created successfully!")

except mysql.connector.Error as e:
    if e.errno == errorcode.ER_TABLE_EXISTS_ERROR:
        print("Table already exists!")
    else:
        print("Failed to create table in MySQL: {}".format(e))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed!")
