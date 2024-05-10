from colorama import Fore


def error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            return Fore.LIGHTRED_EX + str(e)

    return wrapper
