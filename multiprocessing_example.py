from multiprocessing import Process

def heavy_task():
    """Имитация CPU-bound задачи"""
    print("Начало вычислений...")
    total = sum(range(100_000_000))
    print(f"Результат вычислений: {total}")

if __name__ == "__main__":
    print("Запуск основного потока")

    process = Process(target=heavy_task)


    process.start()
    print("Процесс запущен — основной поток продолжает работать")

    # Можно выполнить что-то ещё в основном потоке
    for i in range(3):
        print(f"Основной поток делает что-то ещё... {i+1}")


    process.join()
    print("Вычисления завершены")
