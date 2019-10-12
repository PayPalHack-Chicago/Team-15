import csv
import json

a='salary data.csv'
b='median_.csv'

f = open(b )
reader = csv.reader(f)
reader = csv.reader(f)  #csv reader
next(reader)
dic={}

#for a,b,c,d,e,f,g,h in reader: # loop gives each column a name
#    b=str(b).replace('"','').replace('$','').replace(',','')
#    c=str(c).replace('"','').replace('$','').replace(',','')
#    d=str(d).replace('"','').replace('$','').replace(',','')
#    e=str(e).replace('"','').replace('$','').replace(',','')
#    f=str(f).replace('"','').replace('$','').replace(',','')
#    g=str(g).replace('"','').replace('$','').replace(',','')
#    h=str(h).replace('"','').replace('$','').replace(',','')
#    print(a+','+b+','+c+','+d+','+e+','+f+','+g+','+h)


for a,b,c,d,e,f,g,h in reader:
    dic[a]=[b,c,d]

def major():
    data={}
    user_major=str(input("what's your major? "))
    start_salary=dic[user_major][0]
    mid_salary=dic[user_major][1]
    percent_salary=dic[user_major][2]
    data[Major]=user_major
    data[start_salary]=start_salary
    data[mid_salary]=mid_salary
    data[percent_salary]=percent_salary
    

def tax():
    user_income=int(input("what's your income? "))
    

def retjson():
python2json = json.dumps(a)
print python2json
retjson()
