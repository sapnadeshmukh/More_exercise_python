# Sum of digit by loop 
user=int(input ("enter a number"))
sum=0
num=user
while(num>0):
    rem=num%10
    sum=sum+rem
    num=num//10
print (sum)
if (user% sum==0):
    print("harshad number")
else:
    print("Not harshad number")




print("************************************8")






# Sum of digit by function
def SumOfDigit(user):
    num=user
    sum=0
    while(num>0):
        rem=num%10
        sum=sum+rem
        num=num//10
    print(sum)
    if user%sum==0:
        print("harshad number")
    else:
        print("not harshad number")
value=int(input("enter num"))
SumOfDigit(value)

