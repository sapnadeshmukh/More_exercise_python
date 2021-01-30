list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16] 
list3=list1+list2
i=0
new_list=[]
while (i<len(list3)):
    if list3[i] not in new_list:
        new_list.append(list3[i])
    i=i+1
new_list.sort()
print(new_list)