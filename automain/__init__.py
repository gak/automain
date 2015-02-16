import inspect

def automain(func):
    locale = inspect.stack()[1][0].f_locals
    module = locale.get("__name__", None)
    if module == "__main__":
        locale[func.__name__] = func
        func()
    return func