import csv

file_in = open("student_scores.csv")
file_out = open("sout.csv","w+")
reader = csv.reader(file_in)
writer = csv.writer(file_out,delimiter=',')

fields = next(reader)
writer.writerow(fields)

#starts reading from row 2
for row in reader:
	
	row[1] = int(row[1]) + 10
	writer.writerow([row[0],row[1]])
	
	print(row)
