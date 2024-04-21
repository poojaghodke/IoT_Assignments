#create a table to store employee information

import dbcon


connection = dbcon.get_connection()

query =f"create table employees(empid INT,name VARCHAR(36),dept VARCHAR(40),email VARCHAR(40),salary INT, dateofjoin VARCHAR(16));"
cursor = connection.cursor()
cursor.execute(query)
connection.commit()
cursor.close()
connection.close()


