
def describe(content):
    print(content)

    def wrapper(func):
        def info(*args, **kwargs):
            return func(*args, **kwargs)
        return info
    return wrapper


@describe('content string...')
def test():
    print(1)
