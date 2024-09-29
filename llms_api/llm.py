from config import API_KEY, API_HOST, RAG_PROJECT
import aiohttp


async def llm_query(
        api_key: str,
        api_host: str,
        project: str,
        frame_data: dict,
        video_description: str,
        video_title: str
) -> str:
    '''
    Основной обработчик
    :param api_key: ключ доступа к RestAI
    :param api_host: адрес RestAI
    :param project: название проекта с моделью
    :param frame_data: данные о фрагментах видео
    :param video_description: описание видео
    :param video_title: название видео
    :return:
    '''

    async with aiohttp.ClientSession() as session:

        data = {
            'question': f'Below is information about the video and tags for describing the video, based on this, assign a video tag',
            'system': f'{frame_data}'
        }

        responce = await session.post(
            url=f'{api_host}projects/{project}/question',
            ssl=False,
            headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json"
            },

        )