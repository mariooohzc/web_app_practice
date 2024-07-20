from fastapi import FastAPI
import aiocron
import requests


app = FastAPI()


@aiocron.crontab("*/1 * * * *")
async def self_ping():
    response = requests.get("https://web-app-practice.onrender.com")
    print(f"Health check response: {response.status_code}, testing")


@app.get("/")
async def index():
    return {"message": "testing again"}
