#display the grade

sub1=int(input("enter sub1 : "))
sub2=int(input("enter sub2 : "))
sub3=int(input("enter sub3 : "))
result= int((sub1+sub2+sub3)/3)
print (result)
if (result>=90) and (result<=100):
    print("Grade = A")

elif (result>=80) and (result<=89):
    print("Grade = B")   

elif (result>=70) and (result<=79):
    print("Grade = C")  

elif (result>=60) and (result<=69):
    print("Grade = D")  

else:
    print("Grade = F")           
