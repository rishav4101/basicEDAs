my_dict = {"a":1,"b":2}

##task1: Iterate over all items in this dict
for key,value in my_dict.items():
	print("Key is:",key,"Value is:",value)


my_string = "Hello World"
## Output
##Num of UpperCase Letters: 2
##Num of LowerCase Letters: 8
count1 = 0
count2 = 0

for char in my_string:
	if char.isupper():
		count1 +=1
	elif char.islower():
		count2 +=1
	else:
		pass

#print("Upper Case Count",count1)
#print("LowerCase Count",count2)


## Square of Numbers

def squareList():
	li = []
	for i in range(1,21):
		li.append(i**2)
	return li

#print(squareList())


my_list	= [(2,5),(1,2),(4,4),(2,3)]
my_list.sort(key=lambda x:x[1])
print(my_list)






