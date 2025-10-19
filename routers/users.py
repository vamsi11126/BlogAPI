from fastapi import APIRouter,Depends
from schemas import ShowUser,User
from sqlalchemy.orm import Session
from database import get_db
from repository import user

router=APIRouter(
    prefix='/user',
    tags=["User"]
)

@router.post("/",response_model=ShowUser)
def create_user(request:User,db:Session=Depends(get_db)):
    return user.create(request,db)


@router.get("/{id}",response_model=ShowUser)
def get_user(id:int,db:Session=Depends(get_db)):
    return user.get(id,db)