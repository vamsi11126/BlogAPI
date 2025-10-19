from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status
import models
from database import get_db
from schemas import Blog
def get_all(db:Session=Depends(get_db)):
    blogs=db.query(models.Blog).all()
    return blogs


def create(request:Blog,db:Session=Depends(get_db)):
    new_blog=models.Blog(title=request.title,body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(id,db:Session=Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"BLog with {id} not found")
    db.delete(blog)
    db.commit()
    return "done"

def update(id,request:Blog,db:Session=Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    
    if not blog:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"BLog with {id} not found")
    blog.update(request.dict())
    db.commit()
    
    return "updated" 

def show(id,db:Session=Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
       """
       response.status_code=status.HTTP_404_NOT_FOUND
        return {"detail":f"blog with {id} not found"}
       """
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog with {id} not found")
    return blog