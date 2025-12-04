import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        execution_time = end - start
        print(f"Execution time: {execution_time:.2f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)

if __name__ == "__main__":
    slow_function()