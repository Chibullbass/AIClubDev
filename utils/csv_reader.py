import csv
from collections import defaultdict


async def extract_csv_data(csv_file):
    video_data = {}

    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            video_id = row['video_id']
            video_data[video_id] = {
                'title': row['title'],
                'description': row['description'],
                'tags': row['tags']
            }

    return video_data


async def extract_tags(path: str) -> dict[str: dict[str: list, ...], ...]:
    '''
    Извлечение всех тегов из csv
    :param path: путь до csv файла
    '''
    # Инициализация словаря для хранения данных
    data = defaultdict(lambda: defaultdict(list))

    # Чтение данных из CSV файла
    with open(path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            # Проверяем, что строка содержит нужное количество элементов
            if len(row) == 3:
                category, subcategory, item = row
                # Добавляем элемент в соответствующий подкатегории
                data[category][subcategory].append(item)

    # Преобразуем defaultdict в обычный dict
    data = {k: dict(v) for k, v in data.items()}
    return data
