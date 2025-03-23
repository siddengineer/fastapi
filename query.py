#basic defination

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/items/")
# def read_items(name: str, price: int):
#     return {"name": name, "price": price}


# Optional Query Parameters (Default Values)

# @app.get("/products/")
# def get_product(name: str = "Laptop", price: int = 50000):
#     return {"name": name, "price": price}


#  Query Parameter with Type Conversion

# @app.get("/status/")
# def check_status(is_active: bool):
#     return {"status": is_active}

#  Using Query Parameters with Path Parameters

# @app.get("/users/{user_id}")
# def get_user(user_id: int, active: bool = True):
#     return {"user_id": user_id, "active": active}
