import os

from dotenv import load_dotenv


load_dotenv()


API_HOST = os.environ['API_HOST']
VISION_PROJECT = os.environ['VISION_PROJECT']
RAG_PROJECT = os.environ['RAG_PROJECT']
API_KEY = os.environ['API_KEY']
