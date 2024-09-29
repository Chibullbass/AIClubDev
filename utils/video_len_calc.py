import subprocess


async def get_length(filename: str) -> int:
    """
    рассчет длины видео
    :param filename: Название файла
    :return:
    """
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)

    video_len = round(float(result.stdout))

    return video_len

