"""
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
"""

def round_result(ndigits: int):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, (int, float)):
                return round(result, ndigits)
            return result
        return wrapper
    return decorator

@round_result(2)
def calc(x):
    return x

print(calc(12.432456))
print(calc(12.34))