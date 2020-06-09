import csv
file_in = open("student_scores.csv")
file_out = open("student_scores_out.csv","w+")
reader = csv.reader(file_in)
writer = csv.writer(file_out,delimiter=',')

col_name = next(reader)
writer.writerow(col_name)

for row in reader:
	print(row)
	writer.writerow([row[0],int(row[1])+10])
