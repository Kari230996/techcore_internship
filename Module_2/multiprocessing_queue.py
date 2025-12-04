from multiprocessing import Process, Queue
import time
import random

def producer(queue):
    """Процесс-производитель: кладёт данные в очередь."""
    for i in range(5):
        item = f"item_{i}"
        print(f"[Producer] Отправка: {item}")
        queue.put(item)
        time.sleep(random.uniform(0.5, 1.5))

    queue.put(None)  # Сигнал о завершении
    print("[Producer] Завершил работу.")

def consumer(queue):
    """Процесс-потребитель: получает данные из очереди."""
    while True:
        item = queue.get()
        if item is None:
            print("[Consumer] Завершил работу.")
            break

        print(f"[Consumer] Получено: {item}")
        time.sleep(random.uniform(0.5, 1.0))

if __name__ == "__main__":
    queue = Queue()

    producer_process = Process(target=producer, args=(queue,))
    consumer_process = Process(target=consumer, args=(queue,))

    producer_process.start()
    consumer_process.start()

    producer_process.join()
    consumer_process.join()

    print("Все процессы завершены.")