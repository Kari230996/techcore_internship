import json

config = {
    "project_name": "Techcore Internship",
    "version": "1.0",
    "debug": True,
    "database":
    {
        "host": "localhost",
        "port": 5432,
        "user": "admin",
        "password": "admin",
        
    },
    "allowed_hosts": ["172.0.0.1", "localhost"]

}

with open("config.json", "w", encoding="utf-8") as f:
    json.dump(config, f, indent=4, ensure_ascii=False)

print("Данные успешно записаны в config.json")


with open("config.json", "r", encoding="utf-8") as f:
    loaded_config = json.load(f)

print("\n Прочитанные данные:")
print(loaded_config)