from tabulate import tabulate
from colorama import Fore


def table_decorator(headers=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if headers:
                table = tabulate(result, headers=headers, tablefmt="grid")
            else:
                table = tabulate(result, headers="keys", tablefmt="grid")
            return Fore.LIGHTCYAN_EX + table

        return wrapper

    return decorator
