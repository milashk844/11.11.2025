import datetime
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        result = func(*args, **kwargs)
        end = datetime.datetime.now()
        duration = (end - start).total_seconds()
        print(f"{func.__name__} took {duration:.3f} seconds")
        return result
    return wrapper

@timer
def demo_func():
    time.sleep(5)
    return "Готово!"

print(demo_func())