i=2
while(i<=100):
    j=2
    while(j<i):
        if ((i%j==0)):
            print(i,"not prime")
            break
        j=j+1
    else:
        print(i,"prime")
    i=i+1





