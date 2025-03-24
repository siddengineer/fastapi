from fastapi import FastAPI

app = FastAPI()
products = [
    {"id": 1, "name": "laptop",
"category": "electronics", "price":1500},
    {"id": 2,"name": "Phone",
"category": "electronics", "price":800},
    {"id": 3,"name": "Shoes",
"category": "fashion", "price":500},
]

users = [
    {"id": 1,"name": "sid", "role":"admin"},
    {"id": 2,"name":"sidd", "role":"customer"},
]
@app.get("/products/{product_id}")

def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product
        
    return {"error": "product not found"}



@app.get("/products")    
def filter_products(category: str = None, min_price: int = 0, max_price: int = 999999):
    filtered_products = [ 
        p for p in products
        if (category is None or 
p["category"] == category) and    
            (min_price <= p["price"] <= 
    max_price)
    ]
    return filtered_products
        
@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
    return {"error": "user not found"}

@app.get("/users")
def filter_users(role: str = None):
    if role:
        return [u for u in users if
u["role"] == role]
    return users   
        
    