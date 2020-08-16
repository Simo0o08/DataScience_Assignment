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


    sql = "delete from employee where emp_id=8"
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    print("The Data is Deleted")


except Error as e:
    print(e)
    conn.rollback()

finally:
    if conn is not None and conn.is_connected():
        conn.close()
        print("Connection is Closed")

