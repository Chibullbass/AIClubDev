import os
import asyncio

from config import API_HOST, API_KEY, RAG_PROJECT, VISION_PROJECT, LLM_GENERATOR_PROMT, LLM_FILTER_PROMT, LLM_SORTER_PROMT
from utils.ffmpeg_extractor import extract_audio, extract_frames
from utils.video_len_calc import get_length
from llms_api.vision import vision_query
from llms_api.llm import llm_query
from utils.text_processor import process_text


async def main():
    while True:
        videos = os.listdir('videos')
        if len(videos) > 0:
            print('В кататоге найдено ', len(videos), 'видео.')
            for video in videos:
                print(f'Обработка {video}...')
                video_length =  await get_length(f'videos/{video}')

                await extract_frames(
                    input_video_path=f"videos/{video}",
                    output_folder='frames',
                    interval_seconds=round(video_length/10)
                )

                vision_responce = await vision_query(
                    frames_dir='frames',
                    api_host=API_HOST,
                    api_key=API_KEY,
                    project_name=VISION_PROJECT,
                    video_length=video_length
                )

                result_text = await process_text(vision_responce)

                tag_generator_responce = await llm_query(
                    api_key=API_KEY,
                    api_host=API_HOST,
                    project=RAG_PROJECT,
                    text_data=result_text,
                    query_promt=LLM_GENERATOR_PROMT
                )

                sorted_tags_responce = await llm_query(
                    api_key=API_KEY,
                    api_host=API_HOST,
                    project=RAG_PROJECT,
                    text_data=tag_generator_responce,
                    query_promt=LLM_SORTER_PROMT
                )

                print(sorted_tags_responce)

                return sorted_tags_responce

        else:
            print('В каталоге нету видео.')


if __name__ == '__main__':
    asyncio.run(main())