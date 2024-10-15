async def process_text(dict_text: dict):
    """
    Принимает словарь текста, соеденяет и выводит сплошное полотно текста
    :param dict_text: Словарь с описанием кадров видео
    :return: Сплошной текст
    """
    result_text = ''
    for i in dict_text:
        result_text += dict_text[i]
    return result_text
