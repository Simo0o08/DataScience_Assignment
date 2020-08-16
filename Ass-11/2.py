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

    std = [(1,'Sejal Keswani','Maintenance',20000),(2,'Simmo Keswani','Manager',30000),
    (3,'Ayush Jain','Developer',50000),
    (4,'Avish Jain','Designer',20000),
    (5,'Hemant Bhati','Manager',45000),
    (6,'Jayant Gawali','Tester',45000),
    (7,'Gajendra','Designer',25000),
    (8,'Harsh','Tester',30000),
    (9,'Sandhya','Maintenance',50000),
    (10,'Ayushi ','Developer',40000)]

    query = "INSERT INTO EMPLOYEE VALUES(%s,%s,%s,%s)"

    cursor = conn.cursor()        
    cursor.executemany(query,std) 

    conn.commit()                  
    print("Query has been Inserted")


except Error as e:
    print(e)

finally:
    if conn is not None and conn.is_connected():
        conn.close()
        print("Connection is Closed")