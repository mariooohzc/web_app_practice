from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def index():
    return {
        "message": "changed made, should be something different  ajdf;akljdfl;ajl;fja;jdf;a"
    }
