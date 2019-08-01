def reverse_arg(func):
    def wrapper(t):
        z = t[::-1]
        res = func(z)
        return res
    return wrapper


def show_name_args_res(func):
    def wrapper(t):
        res = func(t)
        print(func.__name__, t, res)
    return wrapper


@show_name_args_res
def division(x):
    return x[0] / x[1]


tp = 10, 5
d = division(tp)
print(d)


