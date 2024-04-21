import dbcon
import add
import delete
import update

ch = int (input("enter a choice 1.add 2.delete 3.update"))

if(ch==1):
    add.add_employees()

elif(ch==2):
    i = input("enter id to delete")
    delete.delete_employees()

elif(ch==3):
   empid= input("enter id to update : ")
   dept= input("enter dept to update : ")
   salary=input("enter salary to update : ")
   update.update_employees(empid,dept,salary)



