import time
from functools import wraps


def time_this(func):
    @wraps(func)  # 保留原始函数的元数据
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        use_time = time.time() - start
        print('[%s] use time:%s' % (func.__name__, use_time))
        return result

    return wrapper


@time_this
def sum_(n):
    total = 0
    for i in range(n):
        total += i
    return total


sum_(100000000)
print(sum_.__name__)
