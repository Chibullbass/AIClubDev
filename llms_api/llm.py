from config import API_KEY, API_HOST
import json
import aiohttp


async def llm_query(
        api_key: str,
        api_host: str,
        project: str,
        text_data: str,
        query_promt: str,
) -> str:
    '''
    Основной обработчик, в функции входит: Генерация, сортировка и фильтрация тэгов.
    :param api_key: ключ доступа к RestAI
    :param api_host: адрес RestAI
    :param project: название проекта с моделью
    :param text_data: данные о фрагментах видео
    :param query_promt: систем промт для запроса
    :return:
    '''

    async with aiohttp.ClientSession() as session:
        data = {
            'question': text_data,
            'system': query_promt
        }


        responce = await session.post(
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            url=f'{api_host}projects/{project}/question',
            ssl=False,
            data=json.dumps(data)
        )
        result_text = await responce.json()

        return result_text["answer"]
