import os

import aiohttp


async def vision_query(frames_dir: str, api_host: str, project_name: str, api_key: str) -> list[str, ...]:
    """
    Отправка запроса vision модели для обработки кадров видео
    :param frames_dir: каталог с кадрами
    :param api_host: адрес rest ai
    :param project_name: название проекта vision модели в rest ai
    :param api_key: api ключ для авторизации в rest ai
    :return:
    """
    for frame in os.listdir('frames'):
        print(frame)

    async with aiohttp.ClientSession() as session:
        responce = await session.post(
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }
            ,
            url=f'{api_host}project/{project_name}/question',
            ssl=False
        )
        print(await responce.json())

    return await responce.json()
