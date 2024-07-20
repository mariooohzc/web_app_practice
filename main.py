from fastapi import FastAPI

import aiocron
import requests


@aiocron.crontab("*/5 * * * *")
async def self_ping():
    response = requests.get("your_fastapi_endpoint")
    print(f"Health check response: {response.status_code}")


app = FastAPI()


@app.get("/")
async def index():
    return {
        "message": "changed made, should be something different  ajdf;akljdfl;ajl;fja;jdf;a"
    }
