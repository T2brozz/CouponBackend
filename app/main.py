from fastapi import FastAPI
from .endpoints import authentication, upload, showData

app = FastAPI()
app.include_router(authentication.router)
app.include_router(upload.router)
app.include_router(showData.router)
