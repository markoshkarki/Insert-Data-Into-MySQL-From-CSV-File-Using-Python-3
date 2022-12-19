import mysql.connector

connection = mysql.connector.connect(
    host='localhost', user='root', password='', database='')
if connection.is_connected():
    db_Info = connection.get_server_info()
    print("Connected to MySQL Server version:", db_Info)
    cursor = connection.cursor()
    mySql_Read_Table = "SELECT * FROM employees.employees_data"
    cursor.execute(mySql_Read_Table)

# Fetch all the records
result = cursor.fetchall()
for i in result:
    print(i)
