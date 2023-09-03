from pydantic import BaseModel, Field, EmailStr

class PostSchema(BaseModel):
    id : int = Field(defailt=None)
    title : str = Field(default = None)
    content : str = Field(default=None)
    class Config:
        scheme_extra = {
            "post_demo": {
                "title": "some content about animals",
                "content" : "some content about animals"
            }
        }
class UserSchema(BaseModel):
    fullname : str = Field(default=None)
    email : EmailStr 
    password : str 
    class Config:
        the_schema = {
            "user_demo":{
                "name": "bek",
                "email": "help@bekbrace.com",
                "password": "123",
                
            }
        }

class UserLoginSchema(BaseModel):
    email : EmailStr
    password : str 
    class Config:
        the_schema = {
            "user_demo":{
                "email": "help@bekbrace.com",
                "password": "123",
                
            }
        }


