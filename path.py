
# without path

# @app.get("/order1")
# def get_order1():
#     return {"order_id": 1, "status": "Shipped"}

# @app.get("/order2")
# def get_order2():
#     return {"order_id": 2, "status": "Processing"}




#path query 
# from fastapi import FastAPI

# # Create FastAPI instance
# app = FastAPI()

# # Sample data: Order IDs mapped to their statuses
# order_statuses = {
#     1: "Shipped",
#     2: "Processing",
#     3: "Delivered"
# }

# @app.get("/orders/{order_id}")
# def get_order(order_id: int):
#     # Fetch the status based on order_id, defaulting to "Not Found"
#     status = order_statuses.get(order_id, "Not Found")
#     return {"order_id": order_id, "status": status}


#path parameters data type

# from fastapi import FastAPI

# # Create FastAPI instance
# app = FastAPI()

# # Example 1: String Parameter
# @app.get("/users/{username}")
# def get_user(username: str):
#     return {"username": username, "message": f"Hello, {username}!"}

# # Example 2: Integer Parameter
# @app.get("/items/{item_id}")
# def get_item(item_id: int):
#     return {"item_id": item_id, "description": f"Item {item_id} details"}

# # Example 3: Float Parameter
# @app.get("/products/{price}")
# def get_product(price: float):
#     return {"price": price, "message": f"Product costs ${price}"}

# # Example 4: Boolean Parameter
# @app.get("/status/{is_active}")
# def check_status(is_active: bool):
#     return {"is_active": is_active, "message": "User is active" if is_active else "User is inactive"}



# incorrect order

# @app.get("/users/{user_id}")  # Dynamic route first
# async def read_user(user_id: int):
#     return {"user_id": user_id}

# @app.get("/users/me")  # Static route after dynamic
# async def read_user_me():
#     return {"user": "Current User"}


# correct order

# @app.get("/users/me")  # Static route first
# async def read_user_me():
#     return {"user": "Current User"}

# @app.get("/users/{user_id}")  # Dynamic route after static
# async def read_user(user_id: int):
#     return {"user_id": user_id}




# Path Parameters with Predefined Values
# from enum import Enum
# from fastapi import FastAPI

# app = FastAPI()

# class ModelName(str, Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"

# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     return {"model_name": model_name}


#multiple paramerters

# @app.get("/users/{user_id}/items/{item_id}")
# async def read_user_item(user_id: int, item_id: str):
#     return {"user_id": user_id, "item_id": item_id}

# Using Path Parameters with Query Parameters

# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "query": q}
