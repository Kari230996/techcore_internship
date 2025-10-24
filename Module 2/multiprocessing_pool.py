from multiprocessing import Pool, cpu_count
import time

def heavy_task(n):
    """Имитация тяжелой CPU-bound задачи"""
    print(f"Запуск задачи {n}")
    total = sum(i * i for i in range(10_000_000))
    print(f"Задача {n} завершена")

    return total

if __name__ == "__main__":
    start = time.time()

    num_cores = cpu_count()
    print(f"Используется ядер: {num_cores}")

    tasks = list(range(1, 11))

    with Pool(processes=num_cores) as pool:
        results = pool.map(heavy_task, tasks)

    print(f"Все задачи завершены. Количество результатов: {len(results)}")
    print(f"Время выполнения: {time.time() - start:.2f} сек.")