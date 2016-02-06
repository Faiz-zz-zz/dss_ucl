import csv
import sys
from turtle import *
import numpy as np
import scipy.misc.pilutil as smp

canvas.setup(160, 160)
gates = open("billgates.csv")
reader = csv.reader(gates)

for row in reader:
	pencolor((int(row[2]), int(row[3]), int(row[4])))
	dot()


#['159', '159', '183', '246', '255']	
