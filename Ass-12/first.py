import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='mydb',
                                         user='root',
                                         password='1234')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
    records =[('webtek',1,3.5,40000),('ardent',2,2,35000),('tcs',3,3,30000),('infosys',4,2.5,30000),('HCL',5,4,45000),('mindtree',6,4.5,55000),('cisco',7,5,60000)
        ,('tcs',8,3,40000),('cisco',9,3,35000),('webtek',10,4,50000)]
    query="Insert into company values(%s,%s,%s,%s)"
    cursor = connection.cursor()
    cursor.executemany(query, records)

    connection.commit()

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")