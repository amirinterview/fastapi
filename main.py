from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Fairphonic"}


@app.get("/addition/{number}")
def addition(x: int, y: int):
    return x + y
