from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

url= 'postgres://bbyxillnzthoti:36a71b444f3b6c16c05781c16ea13c2404404d7585699ac35b1ccd0dfd8e7b7a@ec2-54-235-86-101.compute-1.amazonaws.com:5432/dfrcvrkm39avc9'

#if not os.getenv("url"):
#    raise RuntimeError("DATABASE_URL is not set")

engine = create_engine(url)
db = scoped_session(sessionmaker(bind=engine))
db.execute("CREATE TABLE books (isbn VARCHAR PRIMARY KEY,title VARCHAR NOT NULL,author VARCHAR NOT NULL,year VARCHAR NOT NULL)")

    #create table
