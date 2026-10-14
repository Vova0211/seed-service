from fastapi import FastAPI

from config import settings
from database.MessagesDB import MessagesDB

app = FastAPI()
database = MessagesDB(settings.database_url)


@app.get("/")
def read_root():
    return {"message": settings.greeting}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/db_check")
def db_check():
    with database as db:
        db.execute("SELECT 1")

    return {"status": "ok"}
