# from fastapi import FastAPI
# from pydantic import BaseModel


# app = FastAPI()

# class user(BaseModel):
#     name: str
#     age: int
    
# @app.post("/users/")
# async def create_user(user : User):
#     return {"message": f"User{user.name} added!


# from pydantic import BaseModel

# class UserProfile(BaseModel):
#     name:str
#     age:int
#     email:str
# user = UserProfile(name = "sid",age = 20, email = "sidd")
# print(user)


# basic structure

# from pydantic import BaseModel

# class UserProfile(BaseModel):
#     name:str
#     age:int
#     email:str
#     is_active : bool = True
# user = UserProfile(name = "sid",age = 20, email = "sidd")
# print(user)

#field validator

# from pydantic import BaseModel, field_validator

# class UserProfile(BaseModel):
#     name: str
#     age: int
#     email: str

#     @field_validator('age')
#     def check_age(cls, value):
#         if value < 40:
#             raise ValueError('Age must be at least 18')
#         return value

# UserProfile(name="Rekha", age=50, email="rekha@gmail.com")


# class Address(BaseModel):
#     street: str
#     city: str

# class UserProfile(BaseModel):
#     name: str
#     age: int
#     email: str
#     address: Address

# address = Address(street="461 soraon kauri", city="Prayagraj")
# user = UserProfile(name="Rekha", age= 40, email="rekhashri7342@gmail.com", address=address)
# print(user)


#Parse data
# from pydantic import BaseModel
# import json

# class UserProfile(BaseModel):
#     name: str
#     age: int
#     email: str

# data = '{"name": "Rekha", "age": 40, "email": "rekhashri7354@gmail.com"}'
# user = UserProfile.parse_raw(data)
# print(user)


# from pydantic import BaseModel
# import json

# class UserProfile(BaseModel):
#     name: str
#     age: int
#     email: str


# user = UserProfile(name="Shrinivas", age=22, email="shrinivas3456@gmail.com")

# json_data = user.json()
# print(json_data)

# handling optional and nullable nfields

# from typing import Optional
# from pydantic import BaseModel

# class UserProfile(BaseModel):
#     name: str
#     age: Optional[int] = None
#     email: str






# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class User(BaseModel):
#     name: str
#     age: int

# @app.post("/create_user/")
# async def create_user(user: User):
#     return {"name": "sid", "age": 20}





# from pydantic import BaseModel, Field
# from typing import Optional

# class User(BaseModel):
#     name: str = Field(..., min_length=3)
#     age: int = Field(..., ge=18)
#     email: Optional[str] = None

# @app.post("/create_user/")
# async def create_user(user: User):
#     return {"name": user.name, "age": user.age, "email": user.email}
