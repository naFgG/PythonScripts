# 定义一个装饰器，用于打印函数的执行时间
def timer(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start} seconds to run.")
        return result
    return wrapper


# 使用@符号将timer装饰器应用到fibonacci函数上
@timer
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# 调用fibonacci函数，会自动打印执行时间
fibonacci(10)
