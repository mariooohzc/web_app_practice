from fastapi import FastAPI
import aiocron
import requests
import pkg_resources


app = FastAPI()


@aiocron.crontab("*/1 * * * *")
async def self_ping():
    print("before sending request")
    response = requests.get("https://web-app-practice.onrender.com")
    print("response testing:", response)
    print(f"Health check response: {response.status_code}, testing")


@app.get("/")
async def index():
    installed_packages = pkg_resources.working_set
    for package in installed_packages:
        print(f"{package.key}=={package.version}")

    return {
        "message": "checking if packages are installed and whether poetry installation is working"
    }
