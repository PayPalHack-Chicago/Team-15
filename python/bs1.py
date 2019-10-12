import csv
import os
import psycopg2
#from config import config
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

hostname = '5432'
username = 'postgres'
password = 'w8303040'
database = 'postgres'
command="CREATE TABLE books (isbn VARCHAR PRIMARY KEY,title VARCHAR NOT NULL,author VARCHAR NOT NULL,year VARCHAR NOT NULL)"

myConnection = None

try:
    myConnection = psycopg2.connect(user=username, password=password, dbname=database)
    cur = myConnection.cursor()
    cur.execute(command)
    cur.close()
    myConnection.close()
    
except (Exception, psycopg2.DatabaseError) as error:
        print(error)
finally:
    if myConnection is not None:
        myConnection.close()
 

