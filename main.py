from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import math

app = FastAPI()

def is_valid_number(s: str) -> bool:
    return s.isdigit()  # ONLY digits allowed (no -, no spaces, no floats)

def lcm(x: int, y: int) -> int:
    if x == 0 or y == 0:
        return 0
    return x // math.gcd(x, y) * y  # safer than x*y first

@app.get("/lcm", response_class=PlainTextResponse)
def compute_lcm(x: str = None, y: str = None):
    # Check missing
    if x is None or y is None:
        return "NaN"

    # Strict validation: only digits allowed
    if not is_valid_number(x) or not is_valid_number(y):
        return "NaN"

    try:
        x_int = int(x)
        y_int = int(y)
    except:
        return "NaN"

    return str(lcm(x_int, y_int))

