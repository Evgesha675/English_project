import re

# Список регионов, которые нужно найти
regions_to_find = [
    "Курганская",
    "Свердловская",
    "Тюменская",
    "Челябинская",
    "Ханты-Мансийский (Югра)",
    "Ямало-Ненецкий"
]

# Создаем пустой список для хранения строк с найденными регионами
found_regions = []

# Открываем файл для чтения
with open('regions.txt', 'r', encoding='utf-8') as file:
    # Читаем строки файла
    lines = file.readlines()

# Проходим по каждой строке файла
for line in lines:
    # Ищем значение атрибута data-title
    match = re.search(r'data-title="(.*?)"', line)
    if match:
        # Извлекаем значение data-title
        title = match.group(1)
        # Проверяем, присутствует ли регион в списке, который нужно найти
        if any(region in title for region in regions_to_find):
            # Добавляем строку с найденным регионом в список
            found_regions.append(f"<!-- {title} -->\n")

# Записываем найденные регионы в отдельный файл
with open('found_regions.txt', 'w', encoding='utf-8') as file:
    file.writelines(found_regions)
