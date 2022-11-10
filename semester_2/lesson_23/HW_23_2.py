
import functools
import datetime

def multiply_by_two(func):
    @functools.wraps(func)
    def wrapped(*args):
        return func(*args) * 2
    return wrapped

@multiply_by_two
def multiply(a, b):
    return a * b

print(multiply(2, 10))


def time_in_range(function):
    def wrapped(start, end, now):
        if start <= now <= end:
            return function
    return wrapped

start = datetime.time(7, 0, 0)
end = datetime.time(22, 0, 0)
now = datetime.datetime.now().time()
# print(start, end, now)