
import csv
try:
	with open('C2ImportCalEventSample.csv') as csvfile:
    	readCSV = csv.reader(csvfile, delimiter=',')
    	for row in readCSV:
        	print(row)
        	print(row[0])
        	print(row[0],row[1],row[2],)

except SyntaxError:
	print("SyntaxError")

except TabError:
	print("TabError")