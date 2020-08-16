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

    sql = "update employee set emp_dept='Manager' where emp_name='Simran Jain'"
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    print("The Data is Updated")


except Error as e:
    print(e)
    conn.rollback()

finally:
    if conn is not None and conn.is_connected():
        conn.close()
        print("Connection is Closed")

