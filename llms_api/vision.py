import json
import os

import aiohttp

from config import API_HOST, VISION_PROJECT, API_KEY


async def vision_query(frames_dir: str, api_host: str, project_name: str, api_key: str, video_length: int) -> dict[int: str, ...]:
    """
    Отправка запроса vision модели для обработки кадров видео
    :param frames_dir: каталог с кадрами
    :param api_host: адрес rest ai
    :param project_name: название проекта vision модели в rest ai
    :param api_key: api ключ для авторизации в rest ai
    :return:
    """
    vision_answers = {}
    for frame in os.listdir('../frames'):
        vis = open(f'../frames/{frame}', 'rb')

            #  Отправка запроса к RestAI
        async with aiohttp.ClientSession() as session:
            import base64

            data = {
                'question': f'You virtual assistant you must describe photos in detail.Frames were taken from a {video_length} second long video,at intervals of 10 percent of the video length',
                'image': base64.b64encode(vis.read()).decode('utf-8'),
            }

            responce = await session.post(
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json"
                },
                url=f'{api_host}projects/{VISION_PROJECT}/question',
                ssl=False,
                data=json.dumps(data)
            )
            json_responce = await responce.json()
            print(json_responce)
            vision_answers[int(frame[-8:-4])] = json_responce.get('answer')
            print(int(frame[-8:-4]), responce.status)


    return dict(sorted(vision_answers.items()))


import asyncio
a = asyncio.run(vision_query(
    frames_dir='frames', api_host=API_HOST, project_name=VISION_PROJECT, api_key=API_KEY, video_length=32
))
print(a)