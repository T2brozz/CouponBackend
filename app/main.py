from fastapi import FastAPI

from .endpoints import authentication, upload

app = FastAPI()
app.include_router(authentication.router)
app.include_router(upload.router)