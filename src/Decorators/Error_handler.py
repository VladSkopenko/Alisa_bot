from colorama import Fore


def error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except ValueError:
            print(Fore.LIGHTRED_EX + f"ValueError")  
        except AttributeError:
            print(Fore.LIGHTRED_EX + f"AttributeError")  
        except TypeError:
            print(Fore.LIGHTRED_EX + f"TypeError")  

    return wrapper