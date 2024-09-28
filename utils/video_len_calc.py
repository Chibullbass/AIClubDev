import subprocess


async def get_length(filename: str) -> float:
    """
    Рассчет длины видео
    :param filename: Название файла
    :return: длина видео
    """
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)

    return float(result.stdout)