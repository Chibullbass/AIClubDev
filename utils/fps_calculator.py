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

    if video_len <= 30:
        return 1
    elif video_len <= 300:
        return 10
    elif video_len <= 600:
        return 60
    elif video_len <= 3600:
        return 120
    else:
        return 300
