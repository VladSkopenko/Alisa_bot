def error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except ValueError:
            print(f"ValueError")
        except AttributeError:
            print(f"AttributeError")
        except TypeError:
            print(f"TypeError")
    return wrapper

