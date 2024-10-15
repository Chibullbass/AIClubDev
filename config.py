import os

from dotenv import load_dotenv


load_dotenv()
# Описать каждый параметр окружения

API_HOST = os.environ['API_HOST']
VISION_PROJECT = os.environ['VISION_PROJECT']
RAG_PROJECT = os.environ['RAG_PROJECT']
LLM_GENERATOR_PROMT = os.environ['LLM_GENERATOR_PROMT']
LLM_SORTER_PROMT = os.environ['LLM_SORTER_PROMT']
LLM_FILTER_PROMT = os.environ['LLM_FILTER_PROMT']
API_KEY = os.environ['API_KEY']
