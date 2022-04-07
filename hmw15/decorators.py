from functools import wraps


def save_to_file(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        with open(f"{func.__name__}.txt", "w") as file:
            value_list = func(self, *args, **kwargs)
            for value in value_list:
                file.write(value + '\n')
        return value_list
    return wrapper
