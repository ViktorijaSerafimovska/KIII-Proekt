import time

def do_work():
    while True:
        print("Worker is running background task...")
        time.sleep(10)

if __name__ == "__main__":
    do_work()
