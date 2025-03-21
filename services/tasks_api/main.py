from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

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


@app.get("/")
async def root():
    return {"message": "Allo Ola"}


handle = Mangum(app)
