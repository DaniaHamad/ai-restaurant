from fastapi import FastAPI
from restaurant_core.datetime_lib import get_utc_timestamp


app = FastAPI()


@app.get("/")
async def root():
    return {"timestamp": get_utc_timestamp()}

