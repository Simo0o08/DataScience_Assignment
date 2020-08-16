import mysql.connector
from mysql.connector import Error

conn = None
try:
    conn = mysql.connector.connect(host='localhost',
                                   database='e',
                                   user = 'simran',
                                   password='root',
                                   charset='utf8',
                                   auth_plugin = 'mysql_native_password'
                                   )
    if conn.is_connected():
        print("Connected to Database")
    

    query = "select * from employee"
    cursor = conn.cursor()
    cursor.execute(query)

    rows = cursor.fetchmany(5)   

    print("The 5 data from the given database table are as follows :")
    for row in rows:
        print(row)







except Error as e:
    print(e)

finally:
    if conn is not None and conn.is_connected():
        conn.close()
        print("Connection is Closed")
