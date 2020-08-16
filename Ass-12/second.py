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
        #records =[(1,'ashish','mac',30000),(2,'ashish','mac',30000),(3,'ashish','mac',30000)(4,'ashish','mac',30000),(5,'pawan','civil',45000),(6,'rahul','ee',55000),(7,'vijay','IT',60000)
          #        ,(8,'abhishek','civil',40000),(9,'aditya','ec',35000),(10,'abhay','cs',50000)]
    query="CREATE table company(company_nm varchar(50),emp_id int(50) primary key,yr_of_exp float(20),salary bigint)"
    cursor = connection.cursor()
    cursor.execute(query)

    connection.commit()

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")