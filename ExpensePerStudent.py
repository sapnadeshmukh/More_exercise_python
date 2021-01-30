Number_of_students=int(input("enter number of students"))
Ek_student_ka_kharcha=int(input("enter expense of single student"))
Total_expense=Number_of_students*Ek_student_ka_kharcha
print (Total_expense)
if (Total_expense<=50000):
    print("Hum budget ke andar hain")
else:
    print("Hum budget ke bahar hain")