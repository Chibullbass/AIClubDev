import os

from dotenv import load_dotenv


load_dotenv()


API_HOST = os.environ['API_HOST']
VISION_PROJECT = os.environ['VISION_PROJECT']
LLM_PROJECT = os.environ['LLM_PROJECT']
