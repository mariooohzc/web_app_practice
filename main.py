from fastapi import FastAPI

import aiocron
import requests


app = FastAPI()


@aiocron.crontab("*/1 * * * *")
async def self_ping():
    response = requests.get("your_fastapi_endpoint")
    print(f"Health check response: {response.status_code}")


@app.get("/")
async def index():
    return {
        "message": "changed made, should be something different  ajdf;akljdfl;ajl;fja;jdf;a"
    }
