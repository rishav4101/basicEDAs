import re
string = "June 24"

match = re.match(r"(\w+) (\d+)",string)

if match == None:
	print("Not a valid date string")


print(match.group(2))	

#regex is much better than split
#regex101.com