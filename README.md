# FastAPI Project - Day 1

This is my first FastAPI project. Today, I created a simple API with two endpoints:

- `/` → Returns `{"Hello": "World"}`
- `/items/{item_id}` → Returns item details with an optional query parameter.

## How to Run

1. Install FastAPI and Uvicorn:
   ```
   pip install fastapi uvicorn
   ```
2. Run the server:
   ```
   uvicorn main:app --reload
   ```
3. Open in browser or test in Postman:
   - `http://127.0.0.1:8000/`
   - `http://127.0.0.1:8000/items/1?q=test`

## Future Plans
- Add more routes
- Connect to a database
- Implement authentication

🚀 Stay tuned for updates!

