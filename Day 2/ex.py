# Task 1 was to detect emails
# Task 2 was to print frequency of each word in file


import re
file1 = open("day2-exercise.txt","a+")
reg = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

Dict = {}
a = 0
f = 0
c = 0

# for line in file1:
# 	for word in line.split():
# 		print(word)
# for line in file1:
# 	for word in line.split():
# 		if(re.search(reg,word)):
# 			print(word)

for line in file1:
 	for word in line.split():
 		for wrd, fop in Dict.items():
 			if word == wrd:
 				f = 1
 		if f == 0:
 			for wordd in line.split():
 				if wordd == word:
 					c = c + 1
 			Dict[word] = c
 			c = 0
 		else:
 			f = 0
 			pass


for wo, fl in Dict.items():
	print(wo, ":",fl)