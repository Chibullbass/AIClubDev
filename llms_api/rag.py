import json

import aiohttp
import asyncio

API_Host = "https://rest_ai.spacestation14.ru/projects/fast/question"

loop = asyncio.new_event_loop()
asyncio.set_event_loop(asyncio.new_event_loop())
api_key = "229e11b812604216a0db4e27fe1ed67azlI0GuUb1SN4qGKe-uzGlf8C76mrSZwNS-w0HAJMG40"
json_test = {
  "question": "Как дела?",
  "stream": False,
  "system": "string",
  "colbert_rerank": True,
  "llm_rerank": True,
  "tables": [
    "string"
  ],
  "negative": "string",
  "image": "string",
  "boost": False,
  "lite": False,
  "eval": False,
  "k": 1,
  "score": 0
}

async def request_rag(api_host, api_key, data):
    '''
    Делает запрос в LLM RAG и возвращает тэги
    :param api_host: Хост к RestAI
    :return: Возвращает тэги
    '''
    async with aiohttp.ClientSession() as session:
        responce = await session.post(headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }, url=api_host, ssl=False, data=json.dumps(data))
        data = await responce.json()
        return (data['answer'])


if __name__ == "__main__":
    print(asyncio.get_event_loop().run_until_complete(request_rag(API_Host, api_key, json_test)))
