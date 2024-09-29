import os
import asyncio
from utils.ffmpeg_extractor import extract_audio, extract_frames
from utils.fps_calculator import calc_fps
from utils.csv_reader import extract_csv_data


async def main():
    test_data = await extract_csv_data('train_data_categories.csv')
    print(test_data)
    while True:
        videos = os.listdir('videos')
        if len(videos) > 0:
            print('В кататоге найдено ', len(videos), 'видео.')
            for video in videos:
                print(f'Обработка {video}...')
                interval =  await calc_fps(f'videos/{video}')

                await extract_frames(
                    input_video_path=f"videos/{video}",
                    output_folder='frames',
                    interval_seconds=interval
                )



            break
        else:
            print('В каталоге нету видео.')

if __name__ == '__main__':
    asyncio.run(main())