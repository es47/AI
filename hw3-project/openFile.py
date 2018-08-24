# -*- coding: cp950 -*-
import csv
import os
import sys

pathProg = 'C:\Users\user\Downloads'
os.chdir(pathProg)

if os.getcwd() != pathProg:
    print "EEROR: the file path incorrect."
    sys.exit()

file = open(pathProg + '\TraData.csv', 'r')
csvCursor = csv.reader(file)

for row in csvCursor:
    print row
    
file.close()
