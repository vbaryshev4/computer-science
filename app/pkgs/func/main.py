def print_sum(a, b):
    result = a + b
    return result

def times(func, a, b, c):
    def inner(func, a, b, c):
        t = a
        res = []
        while t != 0:
            res.append(func(b, c))
            t -= 1
        return res
    return inner(func, a, b, c)

def curry(fn, *curried_args):
    def fn(*args):
        arguments = curried_args + args
        return fn(*arguments)
    return fn