#find factorial from 0 to 10
l1= [0,1,2,3,4,5,6,7,8,9,10]

for num in l1:
    i=1
    result =1
    while num>=i:
        result=result*i
        i=i+1
   
    print(f"result={result}") 

