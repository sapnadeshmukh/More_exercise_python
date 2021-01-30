user1=int(input("enter first number"))
user2=int(input("enter second number"))
user3=int(input("enter third number"))
if (user1>user2 and user1 > user3):
    print(user1,"Is greatest number")
elif (user2 >user1 and user2 >user3):
    print(user2,"Is greatest number")
else:
    print(user3,"Is greatest number")
