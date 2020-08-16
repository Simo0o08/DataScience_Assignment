import mysql.connector
from mysql.connector import Error
import pandas as pd

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='mydb',
                                         user='root',
                                         password='1234')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)

    query="SELECT * FROM COMPANY"
    cursor = connection.cursor()
    cursor.execute(query)

        #connection.commit()
    rows = cursor.fetchall()


        #record = cursor.fetchone()
       # print("You're connected to database: ", record)
    results = pd.read_sql_query(query, connection)
    results.to_csv("output.csv", index=False)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")