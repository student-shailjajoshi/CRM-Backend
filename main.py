from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

customers = [
    {"id": 1, "name":"Shailja"},
    {"id":2, "name":"priya"}
]

class Customer(BaseModel):
    id: int
    name : str


    

@app.get("/")
def home():
    return {"message":"CRM Backend"}

@app.get("/customers")
def get_customers():
    return customers

@app.get("/customers/{id}")
def get_customers(id:int):

    for customer in customers:
        if customer["id"] == id:
            return customer
        
    return {"message":"customer not found"}   
 
@app.post("/customers")
def create_customer(customer: Customer):
    customers.append(
        {"id": customer.id, "name": customer.name}
    )
    return customer

@app.put("/customers/{id}")
def update_customer(id:int, customer: Customer):
    for c in customers:
        if c["id"] ==id:
            c["name"] = customer.name
            return c 
        
    return {"message: customer not found"}

@app.delete("/customers/{id}")
def delete_customer(id: int):

    for customer in customers:

        if customer["id"] == id:

            customers.remove(customer)

            return {"message": "Customer deleted"}

    return {"message": "Customer not found"}
        
