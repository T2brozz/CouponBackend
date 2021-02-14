import uvicorn
from app.database import db
from app.models.bill import db

def run_server():
    """Run the uvicorn http server"""
    uvicorn.run("app.main:app", host="localhost", port=8000, reload=True)


if __name__ == '__main__':
    print("Start Server")
    db.Base.metadata.create_all(db.engine)
    # run_server()
