from fastapi import FastAPI
import aiocron
import requests


app = FastAPI()


# @aiocron.crontab("*/2 * * * *")
# async def self_ping():
#     print("before sending request")
#     response = requests.get("https://web-app-practice.onrender.com")
#     print("response testing:", response)
#     print(f"Health check response: {response.status_code}, testing")


@app.get("/")
async def index():
    return {"message": "testing again without job deploy"}
