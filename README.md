# Funfactapi
A simple API that takes a number and returns interesting mathematical properties about it, along with a fun fact
# Number Classification API 🚀

📌 Features

✅ Determines if a number is prime, perfect, or Armstrong.

✅ Classifies numbers as odd or even.

✅ Provides a digit sum and a fun fact from Numbers API.

✅ Handles CORS for cross-origin requests.

✅ Returns structured JSON responses.

✅ Deployed on Google Cloud Platform (GCP).

🚀 Deployment (Google Cloud Platform)

SSH into GCP instance.

Once inside the VM, update system packages and install necessary tools:

sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip git -y

Fetch the Code from GitHub

git clone https://github.com/your-username/Funfactapi.git
cd Funfactapi 



Install dependencies:

pip install -r requirements.txt


Start Gunicorn:

gunicorn gunicorn -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000 main:app 


Start the API Server

gunicorn -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000 main:app

Test the API using Postman or a browser.

Access it via:

http://external-ip:8000/api/classify-number?number=371



