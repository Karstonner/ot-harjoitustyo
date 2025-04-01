import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

FILENAME = os.getenv("CARD_FILE")
FILE_PATH = os.path.join(dirname, "..", "data", FILENAME)

DB_FILENAME = os.getenv("DB_NAME")
DB_FILE_PATH = os.path.join(dirname, "..", "data", DB_FILENAME)
