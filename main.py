from fastapi import FastAPI
import aiocron
import httpx


app = FastAPI()


@aiocron.crontab("*/1 * * * *")
async def self_ping():
    async with httpx.AsyncClient() as client:
        print("before sending request")
        response = await client.get("https://web-app-practice.onrender.com")
        print("response testing:", response)
        print(f"Health check response: {response.status_code}, testing")


@app.get("/")
async def index():
    return {
        "message": "checking if packages are installed and whether poetry installation is working"
    }
