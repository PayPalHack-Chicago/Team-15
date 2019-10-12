import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

url= 'postgres://bbyxillnzthoti:36a71b444f3b6c16c05781c16ea13c2404404d7585699ac35b1ccd0dfd8e7b7a@ec2-54-235-86-101.compute-1.amazonaws.com:5432/dfrcvrkm39avc9'

engine = create_engine(url)
db = scoped_session(sessionmaker(bind=engine))

db.execute('''CREATE TABLE salary ( U_major VARCHAR NOT NULL,
                                    S_M_Salary int NOT NULL,
                                    M-M_Salary int NOT NULL,
                                    Percent_change_from_S_M Salary int NOT NULL,
                                    M_10th_Percentile_Salary int NOT NULL,
                                    M_25th_Percentile_Salary int NOT NULL,
                                    M_75th_Percentile_Salary int NOT NULL,
                                    M_90th_Percentile_Salary int NOT NULL)''')


db.commit()
'''
def main():
    
    #create table
    
    f=open("salary data.csv")     #open file
    reader = csv.reader(f)  #csv reader
    next(reader)
    for a,b,c,d,e,f,g,h in reader:#jump headline
#        print(a,b,c,d,e,f,g,h, end=' ')
        db.execute('''INSERT INTO books (U_major, S_M_Salary, M-M_Salary, Percent_change_from_S_M,M_10th_Percentile_Salary, M_25th_Percentile_Salary,M_75th_Percentile_Salary,M_90th_Percentile_Salary) VALUES (:a,:b,:c,:d,:e,:f,:g)''',{"a":a,"b":b,"c":c,"d":d,"e":e,"f":f,"g":g})
    # for loop input each value into database
    
    print("done")
    db.commit()

'''
