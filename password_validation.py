password=input("enter a password")
if len(password)>=6 and len(password)<=16 :
    if "$"in password:
        if "2"or"8"in password :
            if "A"or"Z" in password:
                print ("strong password")
else:
    print("weak password")
