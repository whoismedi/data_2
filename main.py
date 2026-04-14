from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
import math

app = FastAPI()

def lcm(x: int, y: int) -> int:
    if x == 0 or y == 0:
        return 0
    return x // math.gcd(x, y) * y

def is_valid_number(s: str) -> bool:
    return s.isdigit()

@app.get("/lcm", response_class=PlainTextResponse)
async def compute_lcm(request: Request):
    params = request.query_params

    x = params.get("x")
    y = params.get("y")

    # Missing parameters
    if x is None or y is None:
        return "NaN"

    # Strict validation
    if not is_valid_number(x) or not is_valid_number(y):
        return "NaN"

    x_int = int(x)
    y_int = int(y)

    return str(lcm(x_int, y_int))
