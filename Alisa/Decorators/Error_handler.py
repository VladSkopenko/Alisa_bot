def error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except ValueError as ve:
            print(f"ValueError")
        except AttributeError as a:
            print(f"AttributeError")
        except TypeError:
            print(f"TypeError")
    return wrapper

