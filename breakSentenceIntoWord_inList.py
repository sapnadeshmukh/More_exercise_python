sentence = "NavGurukul is an alternative to higher education reducing the barriers of current formal education system"
i=0
new=[]
while i<len(sentence):
	j=i
	str_count=" "
	while j<len(sentence):
		if sentence[j]==" ":
			break
		else:
			str_count=str_count+sentence[j]
		j=j+1
	new.append(str_count)
	i=j+1
print (new)