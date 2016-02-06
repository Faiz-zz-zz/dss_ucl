import csv
import re

with open("carbon.csv", 'r') as f:
    data = [row for row in csv.reader(f.read().splitlines())]
number = len(data)

names = []

values = []

for i in range(1, number):
	names.append(data[i][1])
	try:
		values.append(map(lambda d:float(d), map(lambda s:re.sub(',','',s),data[i][2:])))
	except:
		pass
	# array = map(lambda s:re.sub(',','',s),data[i][2:])
print values
print names	

