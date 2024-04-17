#program to display face value,place value,reverse of 4-digit number

num = int(input("enter a 4-digit number"))
num1 = num
i = 1000

print("face value :")
while num1>0 :
    q=int(num1/i)
    if num1>9:
        print(q,end=" ")
    else: 
         print(q)   
    num1=num1%i
    i=i/10

num1 = num
i=1000
print("place value :")
while num1>0 :
    q=int(num1/i)
    q=int(q*i)
    if num1>9:
        print(q,"+",end=" ")
    else:
        print(q)    
    num1=num1%i
    i=i/10  

print("reverse value :")
num1=num

while num1>0:
    r=int(num1%10)
    print(r,end=" ")
    num1=int(num1/10)
   


    

