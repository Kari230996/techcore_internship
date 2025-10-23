def read_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            return content
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")
        return None
    
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None
    
    finally:
        print("Закрытие файла")

print("=== Попытка 1: файл существует ===")
content = read_file("config.json")
print(content)

print("\n=== Попытка 2: файл не существует ===")
content = read_file("missing_file.txt")
print(content)
