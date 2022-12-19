import mysql.connector
import csv
from mysql.connector import errorcode

try:
    connection = mysql.connector.connect(
        host='localhost', user='root', password='', database='employees')

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version:", db_Info)
        cursor = connection.cursor(buffered=True)
        cursor.execute('SELECT database();')
        record = cursor.fetchone()
        print("You're connected to database:", record)

        file = open('employees.csv')
        csv_data = csv.reader(file)
        skipHeader = True
        for row in csv_data:
            if skipHeader:
                skipHeader = False
                continue
            cursor.execute(
                'INSERT INTO employees_data(first_name, last_name, company_name, address, city, country, state, zip, phone1, phone2, email, web)' 'VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', row)
            connection.commit()
        print(cursor.rowcount,
              "record(s) inserted successfully into employees_data table!")

        # mySql_Insert_Into_Table_Query = "LOAD DATA INFILE 'employees.csv' INTO TABLE employees_data FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES (first_name, last_name, company_name, address, city, country, state, zip, phone1, phone2, email, web)"
        # cursor.execute(mySql_Insert_Into_Table_Query)


except mysql.connector.Error as e:
    print('Failed to insert record into employees_data table: {}' .format(e))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed!")
