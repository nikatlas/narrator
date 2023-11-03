from functools import wraps
from time import time

ELAPSED_SECONDS = []


def timer_func(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print(f"func:{f.__name__} args:[{args}, {kw}] took: {te-ts} sec")
        ELAPSED_SECONDS.append(te - ts)
        return result

    return wrap
