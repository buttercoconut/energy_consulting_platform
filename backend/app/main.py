# app/main.py
from fastapi import FastAPI
from . import routers

app = FastAPI(title="Energy Consulting Platform API")

# Include routers
app.include_router(routers.users.router, prefix="/users", tags=["users"])
app.include_router(routers.energy.router, prefix="/energy", tags=["energy"])

# Root endpoint
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Energy Consulting Platform API"}
