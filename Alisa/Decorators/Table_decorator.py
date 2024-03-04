from tabulate import tabulate
from colorama import Fore


def table_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        table = tabulate(result, headers="keys", tablefmt="grid")
        return Fore.LIGHTCYAN_EX + table

    return wrapper


def table_decorator_for_note(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        headers = ["Id", "Title", "Date of last update", "Note"]
        table = tabulate(result, headers=headers, tablefmt="grid")

        return Fore.LIGHTCYAN_EX + table

    return wrapper


def table_decorator_for_record(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        headers = ["Name", "Company", "Email", "Birthday", "Phone", "Tags", "Address"]
        table = tabulate(result, headers=headers, tablefmt="grid")
        return Fore.LIGHTCYAN_EX + table

    return wrapper
