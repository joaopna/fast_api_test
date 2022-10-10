from colorama import init
from fastapi import FastAPI
from pydantic import BaseModel
import time


class ParenthesisRequest(BaseModel):
    sequence: str


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World", "stage": "test"}


@app.get("/fibonacci/{n}")
async def fibonacci(n):
    result = 1
    previous = 1
    for _ in range(2, int(n)):
        next_previous = result
        result = previous + result
        previous = next_previous
    return result


@app.post("/parenthesis")
async def parenthesis(request: ParenthesisRequest):
    initial_time = time.time()
    previous_length = len(request.sequence)
    new_sequence = request.sequence.replace("()", "")
    new_sequence = new_sequence.replace("[]", "")
    new_sequence = new_sequence.replace("{}", "")

    while 0 < len(new_sequence) != previous_length:
        previous_length = len(new_sequence)
        new_sequence = new_sequence.replace("()", "")
        new_sequence = new_sequence.replace("[]", "")
        new_sequence = new_sequence.replace("{}", "")

    return {"is_valid": len(new_sequence) == 0,
            "processing_time": time.time() - initial_time}
