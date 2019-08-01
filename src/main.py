import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request

from api import api

# init_db(db_session)
# from core import config

app = FastAPI()


app.include_router(api)

if __name__ == "__main__":
    # uvicorn.run(app, host="127.0.0.1", port=5000, log_level="info")
    uvicorn.run(app, log_level="info")
