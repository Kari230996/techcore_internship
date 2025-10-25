import asyncio

async def worker(name: str, lock: asyncio.Lock):
    print(f"{name} ожидает доступ к ресурсу...")
    async with lock:
        print(f"{name} получил доступ к ресурсу...")
        await asyncio.sleep(1)
        print(f"{name} освободил доступ к ресурсу...")

async def main():
    lock = asyncio.Lock()

    tasks = [worker(f"Task-{i}", lock) for i in range(1, 11)] # 10 задач
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
