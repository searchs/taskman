from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
from datetime import datetime as dt, timezone as tz


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health-check/")
async def health_check():
    return {"message": "OK"}


@app.get("/app", tags=["basics"])
async def generics():
    return {"app_details": "fastapi vue", "time": dt.now(tz.utc)}


@app.get("/")
async def root():
    return {"message": "Allo Ola"}


handle = Mangum(app)
