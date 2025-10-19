from fastapi import FastAPI
import models
from database import engine
from routers import blog,users,login
app=FastAPI() 
models.Base.metadata.create_all(bind=engine)
app.include_router(blog.router)
app.include_router(users.router)
app.include_router(login.router)

