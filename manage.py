import os
import asyncio
from utils.ffmpeg_extractor import extract_audio, extract_frames
from utils.video_len_calc import get_length


async def main():
    while True:
        videos = os.listdir('videos')
        print('В кататоге найдено ', len(videos), 'видео.')
        for video in videos:
            print(f'Обработка {video}...')
            video_length =  await get_length(f'videos/{video}')
            print(f'Продолжительность {video_length}')



            await extract_frames(
                input_video_path=f"videos/{video}",
                output_folder='frames',
                interval_seconds=6
            )


if __name__ == '__main__':
    asyncio.run(main())