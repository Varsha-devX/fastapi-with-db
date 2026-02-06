from pydantic import BaseModel


class userschema(BaseModel):
    email:str
    password:str
