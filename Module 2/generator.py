def read_large_log(file_path, keyword=None):
    """Генератор, возвращает строки по одной. 
    Если указан keyword — возвращает только строки, содержащие это слово."""
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.rstrip("\n")
            if not keyword or keyword in line:
                yield line


for entry in read_large_log("server.log", keyword="ERROR"):   # файл не существует, но код выполняет задачу
    print(entry)
