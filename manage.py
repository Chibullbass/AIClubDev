import os
import asyncio

from config import API_HOST, API_KEY, VISION_PROJECT
from utils.ffmpeg_extractor import extract_audio, extract_frames
from utils.video_len_calc import get_length
from utils.csv_reader import extract_csv_data
from llms_api.vision import vision_query


async def main():
    test_data = await extract_csv_data('train_data_categories.csv')
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

                print(vision_responce)

            break
        else:
            print('В каталоге нету видео.')


if __name__ == '__main__':
    asyncio.run(main())