from fastapi import FastAPI, Query
from fastapi.responses import PlainTextResponse
import math

app = FastAPI()

def lcm(x:int, y:int) -> int:
    if x == 0 or y == 0:
        return 0
    return abs(x * y) // math.gcd(x,y)
    

@app.get("/madina_meiramova_2001_gmail_com", response_class=PlainTextResponse)
def compute_lcm(x:str=None, y:str=None):
    try:
        x_int = int(x)
        y_int = int(y)
        if x_int < 0 or y_int < 0:
            raise ValueError
    except (ValueError, TypeError):
        return "NaN"
    return str(lcm(x_int, y_int))

