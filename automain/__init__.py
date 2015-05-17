import inspect

def automain(func):
    exc_info = None

    try:
        locale = inspect.stack()[1][0].f_locals
        module = locale.get("__name__", None)
        if module == "__main__":
            locale[func.__name__] = func
            func()
        return func
    except:
        # skip the entry in the traceback that stems from within automain by raising the next entry
        import sys
        exc_info = sys.exc_info() # == exc_type, exc_value, exc_traceback
        raise exc_info[0], exc_info[1], exc_info[2].tb_next
    finally:
        # clean up according to: https://docs.python.org/2/library/sys.html#sys.exc_info
        del exc_info

