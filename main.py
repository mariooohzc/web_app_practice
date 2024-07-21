from fastapi import FastAPI
import aiocron
import requests
import asyncio


app = FastAPI()


@aiocron.crontab("*/1 * * * *")
async def self_ping():
    print("before sending request")
    response = requests.get("https://web-app-practice.onrender.com")
    print("response testing:", response)
    print(f"Health check response: {response.status_code}, testing")


@app.get("/")
async def index():
    return {
        "message": "checking if packages are installed and whether poetry installation is working"
    }


asyncio.get_event_loop().run_forever()
