
import json
import csv

a='salary data.csv'
b='median_.csv'
c='output-v1.1.csv'
f = open(c)

box=[]
reader1 = csv.reader(f)
for i in reader1:
    box.append(i)
    
print(box[0])
