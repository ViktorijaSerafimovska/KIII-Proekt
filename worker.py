import time

def do_work():
    while True:
        print("Worker is running background task...")
        # Овде може да додадеш каква било задача, на пример читање од редица, обработка итн.
        time.sleep(10)  # спиј 10 секунди пред повторно да работи

if __name__ == "__main__":
    do_work()
