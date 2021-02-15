import uvicorn
from app.database import db
import app.main


def run_server():
    """Run the uvicorn http server"""
    print("test")
    uvicorn.run("app.main:app", host="localhost", port=8000, reload=True)


if __name__ == '__main__':
    print("Start Server")
    db.Base.metadata.create_all(db.engine)
    run_server()
