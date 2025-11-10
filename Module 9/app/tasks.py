from core.celery_app import celery_app
import sys
from pathlib import Path


sys.path.append(str(Path(__file__).resolve().parent.parent))


@celery_app.task()
def add(x, y):
    return x + y


if __name__ == "__main__":
    result = add.delay(2, 3)
    print("Отправлена задача, ID:", result.id)
