#maximum of three numbers

num1=int(input("enter num1 : "))
num2=int(input("enter num2 : "))
num3=int(input("enter num3 : "))

if num1>num2:
    if num1>num3:
        print(f"num1 is greater={num1}")
    else:
        print(f"num3 is greater={num3}")    

else:
    if num2<num3:
        print(f"num3 is greater={num3}")
    else: 
        print(f"num2 is greater={num3}")
     
