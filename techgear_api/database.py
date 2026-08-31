import os
from pathlib import Path

from dotenv import load_dotenv
from pymongo import MongoClient


BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR / ".env")


MONGODB_URI = os.getenv("MONGO_URL")
DATABASE_NAME = os.getenv("DATABASE_NAME", "techgear")


client = MongoClient(MONGODB_URI)

db = client[DATABASE_NAME]

productos_collection = db["productos"]

pedidos_collection = db["pedidos"]