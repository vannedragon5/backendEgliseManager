from fastapi import FastAPI, Request
import requests, uuid

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Backend pawaPay en ligne 🚀"}

@app.post("/initiate-payment")
def initiate_payment(data: dict):
    payload = {
        "requestId": str(uuid.uuid4()),
        "currency": data["currency"],
        "amount": data["amount"],
        "customer": {
            "msisdn": data["msisdn"],
            "network": data["network"]
        },
        "callbackUrl": "https://tonbackend.onrender.com/webhook"
    }

    headers = {
        "Authorization": "Bearer TA_CLE_API_SECRETE",
        "Content-Type": "application/json"
    }

    response = requests.post("https://api.pawapay.io/payments", json=payload, headers=headers)
    return response.json()

@app.post("/webhook")
async def webhook(request: Request):
    body = await request.json()
    print("Callback reçu:", body)
    return {"status": "ok"}
