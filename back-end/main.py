from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


# cors config
origins = [
    "http://localhost",
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#wazny kod
fake_db = {
    'skurek':'uczeń',
    'dpietrzyk':'nauczyciel'
}

@app.get("/getUserRole")
async def getUserRole(login: str):
    return fake_db[login]