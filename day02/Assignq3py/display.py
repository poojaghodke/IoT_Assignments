import dbcon

ch = int (input("enter a choice 1.print all employees 2.employees of given dept 3.employee with highest salary 4.employee with lowest salary : "))
connection = dbcon.get_connection()

if(ch==1):
    query = f"select *from employees;"
   

elif(ch==2):
    dept= input("enter dept  : ")
    query = f"select *from employees where dept='{dept}';"

elif(ch==3):
    query = f"select *from employees order by salary DESC;"

elif(ch==4):
    query = f"select *from employees order by salary ASC;"

cursor = connection.cursor()
cursor.execute(query)
#connection.commit()
records = cursor.fetchall()    
for i in records:
    print("Employee Id : ", i[0])
    print("Employee Name : ", i[1])
    print("Employee Dept : ", i[2])
    print("Employee Salary : ", i[3])
    print("Employee Date of joining: ", i[4])
   
cursor.close()
connection.close()



