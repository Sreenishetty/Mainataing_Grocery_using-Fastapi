from pydantic import BaseModel, Field, EmailStr


class PostSchema(BaseModel):
    id : int = Field(default=None)
    title : str = Field(default=None)
    content : str = Field(default=None)

    class Config:
        schema_extra = {
            "example" : {
                "title": "Any kind of items from shopping can be added",
                "content": "some content about the item"
            }
        }

class UserSchema(BaseModel):
    name : str = Field(default=None)
    email : EmailStr = Field(default=None)
    password : str = Field(default=None)
    class Config:
        schema_extra = {
            "example":{
                "name" : "sreeni",
                "email": "sreeni@123.com",
                "password": "123"
            }
        }

class UserLoginSchema(BaseModel):
    email : EmailStr = Field(default=None)
    password : str = Field(default=None)
    class Config:
        schema_extra = {
            "example":{
                "email": "sreeni@123.com",
                "password": "123"
            }

        }
