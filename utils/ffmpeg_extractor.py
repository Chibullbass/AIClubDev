import ffmpeg # скачать ffmpeg-python
from pathlib import Path
from typing import Union


async def extract_audio(input_video_path: str, output_audio_path: str) -> None:
    """
    Извлекает аудио из видео и сохраняет его в формате MP3.

    :param input_video_path: Путь к исходному видеофайлу
    :param output_audio_path: Путь для сохранения аудиофайла в формате MP3
    """
    try:
        # Используем ffmpeg для извлечения аудио
        ffmpeg.input(input_video_path).output(output_audio_path, format='mp3').run()
        print(f"Успешно извлечено аудио: {output_audio_path}")
    except Exception as e:
        print(f"Ошибка при извлечении аудио: {e}")


async def extract_frames(input_video_path: str, output_folder: Union[str, Path], interval_seconds: int | float) -> None:
    """
    Извлекает кадры из видео с заданной периодичностью.

    :param input_video_path: Путь к видеофайлу
    :param output_folder: Папка для сохранения извлеченных кадров
    :param interval_seconds: Интервал между кадрами в секундах (может быть целым или дробным числом)
    """
    output_folder = Path(output_folder)  # Преобразуем в Path объект

    try:
        # Проверяем, существует ли папка для сохранения кадров
        output_folder.mkdir(parents=True, exist_ok=True)

        # Строим команду ffmpeg для извлечения кадров
        (
            ffmpeg
            .input(input_video_path, ss=0)
            .filter('fps', fps=1 / interval_seconds)  # Один кадр каждые `interval_seconds` секунд
            .output(str(output_folder / 'frame_%04d.png'))  # Сохранение кадров в формате PNG
            .run()
        )
        print(f"Успешно извлечены кадры в папку: {output_folder}")
    except Exception as e:
        print(f"Ошибка при извлечении кадров: {e}")


# # Пример использования функций
# input_video: str = 'video.mp4'  # Путь к видеофайлу
# output_audio: str = 'audio.mp3'  # Путь для сохранения MP3-файла
# output_frames_folder: Path = Path('frames')  # Папка для сохранения кадров
# interval_seconds: int = 60  # Интервал между кадрами (например, каждые 10 секунд)
#
# # Извлекаем аудио
# extract_audio(input_video, output_audio)
#
# # Извлекаем кадры каждые 10 секунд
# extract_frames(input_video, output_frames_folder, interval_seconds)
