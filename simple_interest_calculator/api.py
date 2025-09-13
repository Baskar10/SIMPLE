from fastapi import FastAPI
from pydantic import BaseModel
from .calculator import calculate_simple_interest

app = FastAPI()

class SIRequest(BaseModel):
    principal: float
    rate: float
    time: float

@app.post("/calculate")
def calculate_si(data: SIRequest):
    si, total = calculate_simple_interest(data.principal, data.rate, data.time)
    return {"simple_interest": si, "total_amount": total}
