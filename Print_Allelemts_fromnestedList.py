list = [[1,2,3], [5,8,9], [4,3,77,521,31,311]]
i=0
while(i<len(list)):
    j=0
    while(j<len(list[i])):
        print(list[i][j])
        j=j+1
    i=i+1
    print("************")
