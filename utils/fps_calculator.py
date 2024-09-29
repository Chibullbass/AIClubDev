import subprocess


async def calc_fps(filename: str) -> int:
    """
    Рассчет частоты сохранения кадров
    :param filename: Название файла
    :return: интервал между кадрами видео
    """
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)

    video_len = float(result.stdout)
    print(video_len)

    return round(video_len/10)
