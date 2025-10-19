from fastapi import APIRouter,Depends,status
from typing import List
from schemas import showBlog,Blog
from database import get_db
from sqlalchemy.orm import Session
from repository import blog
from schemas import User
from oauth2 import get_current_user
router=APIRouter(
    tags=["Blogs"],
    prefix='/blog'
)


@router.get("/",response_model=List[showBlog])
def all(db:Session=Depends(get_db),get_current_user:User=Depends(get_current_user)):
    return blog.get_all(db)

@router.get('/{id}',status_code=200,response_model=showBlog)
def show(id,db:Session=Depends(get_db),get_current_user:User=Depends(get_current_user)):
   return blog.show(id,db)


@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request:Blog,db:Session=Depends(get_db),get_current_user:User=Depends(get_current_user)):
    return blog.create(request,db)


@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db:Session=Depends(get_db),get_current_user:User=Depends(get_current_user)):
    return blog.destroy(id,db)

@router.put("/{id}",status_code=status.HTTP_202_ACCEPTED)
def update(id,request:Blog,db:Session=Depends(get_db),get_current_user:User=Depends(get_current_user)):
    return blog.update(id,request,db)