from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
db_path = "/tmp/blog.db" if os.getenv("RENDER") else "./blog.db"

engine = create_engine(f"sqlite:///{db_path}", connect_args={"check_same_thread": False})
Base=declarative_base()

sessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)
def get_db():
    db=sessionLocal()
    try:
        yield db
    finally :
        db.close()
