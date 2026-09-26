import logging

from config import settings
from fastapi import FastAPI

logging.basicConfig(filename='logs/main.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
app = FastAPI()

try:
    settings.greeting
except:
    logging.error("Env variable is not exist")
    raise EnvironmentError("GREETING is no exist")

@app.get("/")
def read_root():
    logging.info("User get greeting")
    return {"message": settings.greeting}


@app.get("/health")
def health_check():
    logging.info("User check health")
    return {"status": "ok"}

# @app.get("/db_check")
# def db_check():
#     logging.info("User check database")
#
#     db_url = os.environ["DATABASE_URL"]
#     with psycopg.connect(db_url) as db:
#         db.execute("SELECT 1")
#
#     return {"status": "ok"}