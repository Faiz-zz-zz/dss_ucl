import csv
import re

def regressionLine(array):
	yearArray = [i for i in range(1999, 2016)]
	xDash = sum(yearArray)/len(yearArray)
	n = len(array)
	yDash = sum(array)/n
	b = ((n*sum([a*b for a, b in zip(yearArray, array)]))-(sum(array)*sum(yearArray)))/((n*sum(map(lambda x: x**2, yearArray)))-((sum(yearArray))**2))
	a = ((sum(array))-b*sum(yearArray))/n
	for i in [2020, 2025, 2030]:
		array.append(a+b*i)

with open("crime_data.csv", 'r') as f:
    data = [row for row in csv.reader(f.read().splitlines())]
number = len(data)

names = []

values = []

ind = 0
for i in range(1, number):
	try:
		array = map(lambda s:re.sub(',','',s),data[i][2:])
		array = map(lambda d:float(d), array)
		ind = len(array)
		regressionLine(array)
		values.append(array)
		names.append(data[i][1])		
	except:
		# print data[i]
		pass
	# # array = map(lambda s:re.sub(',','',s),data[i][2:])

# print values
# print names

for i in range(0, ind+3):
	maxima = 0
	for j in range(0, len(names)):
		maxima = max(maxima, values[j][i])
	for j in range(0, len(names)):
		values[j][i] = (values[j][i]/maxima)*100	

print values
print names	
