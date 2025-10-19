from pydantic import BaseModel
from typing import List

class Blog(BaseModel):
    title:str
    body:str
    

class ShowUser(BaseModel):
    name:str
    email:str
    blogs:List[Blog]=[]
    class Config():
        from_attributes=True
 
class showBlog(Blog):
    title:str
    body:str
    creator:ShowUser
    class Config():
        from_attributes=True

class User(BaseModel):
    name:str
    email:str
    password:str

class Login(BaseModel):
    username:str
    password:str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None

