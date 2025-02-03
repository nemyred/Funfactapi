from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# Enable CORS (Allow all origins for now, can be restricted later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to specific domains if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    if n < 2:
        return False
    return sum([i for i in range(1, n) if n % i == 0]) == n

def is_armstrong(n: int) -> bool:
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n

@app.get("/api/classify-number")
def classify_number(number: int = Query(..., description="The number to classify")):
    try:
        # Determine properties
        properties = []
        if is_armstrong(number):
            properties.append("armstrong")
        properties.append("even" if number % 2 == 0 else "odd")

        # Get fun fact
        fun_fact_url = f"http://numbersapi.com/{number}/math"
        fun_fact = requests.get(fun_fact_url).text

        # JSON response
        return {
            "number": number,
            "is_prime": is_prime(number),
            "is_perfect": is_perfect(number),
            "properties": properties,
            "digit_sum": sum(map(int, str(number))),
            "fun_fact": fun_fact
        }
    except Exception as e:
        return {"number": number, "error": True, "message": str(e)}

