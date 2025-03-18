# from fastapi import FastAPI

# # Create an instance of FastAPI
# app = FastAPI()

# # Define a simple GET route
# @app.get("/")
# async def read_root():
#     return {"message": "Hello, World!"}
from fastapi import FastAPI

# Create FastAPI instance
app = FastAPI()

# Define the root route
@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

# Define a dynamic route with path parameters
@app.get("/greet/{name}")
async def greet(name: str):
    return {"message": f"Hello, {name}!"}

# Define a route with query parameters
@app.get("/greet")
async def greet(name: str = "Guest"):
    return {"message": f"Hello, {name}!"}
