import time
from functools import wraps


def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] вызван метод {func.__name__}()")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__}() вернул: {result}")
        return result
    return wrapper


def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"[PERFORMANCE] {func.__name__}: {elapsed:.6f} sec")
        return result
    return wrapper


def repeat(count):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(count):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator
