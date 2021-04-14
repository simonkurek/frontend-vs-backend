from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


fake_db = {
    'skurek':'student',
    'dpietrzyk':'teacher'
}

@app.get("/getUserRole")
async def getUserRole(login: str):
    return fake_db[login]