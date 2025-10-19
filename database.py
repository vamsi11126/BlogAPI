from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
engine = create_engine(r"sqlite:///C:/Users/vamsi/Desktop/FastAPI/BLog/blog.db", connect_args={"check_same_thread": False})

Base=declarative_base()

sessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)
def get_db():
    db=sessionLocal()
    try:
        yield db
    finally :
        db.close()
