list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1] 
i=0
new_list=[]
while (i<len(list1)):
    if list1[i] in list2 :
        new_list.append(list1[i])
    i=i+1
new_list.sort()
print (new_list)