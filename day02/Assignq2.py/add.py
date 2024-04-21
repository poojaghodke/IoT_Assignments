#create a table to store employee information

import dbcon

def add_employees():
    connection = dbcon.get_connection()

    empid = int(input("Enter employee id : "))
    name = input("Enter name : ")
    dept = input ("Enter department name : ")
    email = input ("Enter email : ")
    salary = int(input("Enter salary : "))
    dateofjoin = input("date of joining : ")

    query =f"insert into employees values({empid},'{name}','{dept}','{email}',{salary},'{dateofjoin}');"

    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()