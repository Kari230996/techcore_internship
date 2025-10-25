import json
import aiofiles
import asyncio


async def config_json(config):
    async with aiofiles.open("config.json", "w", encoding="utf-8") as f:
        # сериализуем вручную
        data = json.dumps(config, indent=4, ensure_ascii=False)
        await f.write(data)
    print("Данные успешно записаны в config.json")

    async with aiofiles.open("config.json", "r", encoding="utf-8") as f:
        content = await f.read()
        loaded_config = json.loads(content)  # десериализация вручную

    print("\nПрочитанные данные:")
    print(loaded_config)


async def main():
    config = {
        "project_name": "Techcore Internship",
        "version": "1.0",
        "debug": True,
        "database": {
            "host": "localhost",
            "port": 5432,
            "user": "admin",
            "password": "admin",
        },
        "allowed_hosts": ["127.0.0.1", "localhost"]
    }

    await config_json(config)


if __name__ == "__main__":
    asyncio.run(main())
