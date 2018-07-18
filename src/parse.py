import csv

filename = '/Users/yuzeyuan/Dataset_FudanWiFi09/File1_AccessLogs.csv' #read file
with open(filename) as f:
    reader = csv.reader(f)
    data = list(reader)

building = [[],[],[],[],[],[]]
for i in range(414,2000):
	count = [0,0,0,0,0,0,0]
	for row in data[1:2500]:
		if (i >= int(row[1]) and i < (int(row[1])+int(row[2]))):
			count[int(row[3][0])-2] += 1
	for index in range(0,6):
		temp = [i,count[index]]
		building[index].append(temp)

filename = '/Users/yuzeyuan/Dataset_FudanWiFi09/result.txt' #write to file
with open(filename,'a') as f:
	for bld in building:
		f.write(str(bld))
		f.write("\n")
		f.write("\n") 
		f.write("\n")  
		
