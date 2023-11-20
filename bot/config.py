import os
from dotenv import load_dotenv

load_dotenv()

# Variables from the .env
BOT_TOKEN = os.environ["BOT_TOKEN"]
PREFIX = os.environ["PREFIX"]
OWNER_ID = int(os.environ["OWNER_ID"])
SUPPORT_ID = int(os.environ["SUPPORT_ID"])
DEBUG = bool(os.environ["DEBUG"])
