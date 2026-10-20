import time

class Operation:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f"[OPERATION] Начало операции: {self.name}")
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        elapsed = time.perf_counter() - self.start
        print(f"[OPERATION] Завершение операции: {self.name} ({elapsed:.6f} sec)")
        if exc_type is not None:
            print(f"[OPERATION] Произошла ошибка: {exc_value}")
        return False
