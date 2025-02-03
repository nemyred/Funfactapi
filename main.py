from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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
    # Validate number (Must be an integer)
    if not isinstance(number, int):
        raise HTTPException(status_code=400, detail="Invalid input. Number must be an integer.")

    # Determine properties
    properties = []
    if is_armstrong(number):
        properties.append("armstrong")
    properties.append("even" if number % 2 == 0 else "odd")

    # Get fun fact
    fun_fact_url = f"http://numbersapi.com/{number}/math"
    try:
        fun_fact_response = requests.get(fun_fact_url)
        if fun_fact_response.status_code == 200:
            fun_fact = fun_fact_response.text
        else:
            fun_fact = "No fun fact available."
    except requests.exceptions.RequestException:
        fun_fact = "Fun fact service unavailable."

    # Return JSON response with proper types
    return {
        "number": number,
        "is_prime": bool(is_prime(number)),   # Ensure boolean
        "is_perfect": bool(is_perfect(number)),  # Ensure boolean
        "properties": properties,  # Ensure list/array
        "digit_sum": sum(map(int, str(abs(number)))),  # Ensure numeric
        "fun_fact": str(fun_fact)  # Ensure string
    }
