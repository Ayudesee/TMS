from functools import wraps


def save_to_file(filename: str = "test.txt"):
    """
    decorator for saving given text in directory.\n
    decorated function should return list of strings that will be saved into the file\n
    :arg filename
        should specify filepath
    """

    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            with open(f"{filename}", "w") as file:
                result = func(self, *args, **kwargs)
                for value in result:
                    file.write(value + '\n')
            return result

        return wrapper

    return decorator
