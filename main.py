import os
import logging

from fastapi import FastAPI
from dotenv import load_dotenv

logging.basicConfig(filename='logs/main.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
app = FastAPI()
load_dotenv()

# Приветствие сервис берёт из окружения.
# Нет переменной GREETING — сервис не стартует.
greeting: str
try:
    greeting = os.environ["GREETING"]
except:
    logging.error("Env variable is not exist")
    raise EnvironmentError("GREETING is no exist")

@app.get("/")
def read_root():
    logging.info("User get greeting")
    return {"message": greeting}


@app.get("/health")
def health_check():
    logging.info("User check health")
    return {"status": "ok"}
