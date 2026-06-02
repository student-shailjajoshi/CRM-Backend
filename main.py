from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "CRM Backend Running!"}

@app.get("/customers")
def get_customers():
    customers = [
        {"id": 1, "name": "Priya Sharma", "email": "priya@gmail.com", "status": "New"},
        {"id": 2, "name": "Rahul Verma", "email": "rahul@gmail.com", "status": "Follow-up"},
        {"id": 3, "name": "Sneha Gupta", "email": "sneha@gmail.com", "status": "Closed"},
    ]
    return customers