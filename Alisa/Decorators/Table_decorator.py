from tabulate import tabulate
from colorama import Fore


def table_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        table = tabulate(result, headers="keys", tablefmt="grid")
        return Fore.LIGHTCYAN_EX + table

    return wrapper
