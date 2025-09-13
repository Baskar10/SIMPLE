from fastapi import FastAPI
from pydantic import BaseModel
from .calculator import calculate_simple_interest

app = FastAPI(title="Simple Interest Calculator API")

class InterestRequest(BaseModel):
    principal: float
    rate: float
    time: float

@app.post("/calculate")
def calculate_si(req: InterestRequest):
    si, total = calculate_simple_interest(req.principal, req.rate, req.time)
    return {"simple_interest": si, "total_amount": total}
