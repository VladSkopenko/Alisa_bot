def error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except ValueError:
            print(f"ValueError")  # todo red color add
        except AttributeError:
            print(f"AttributeError")  # todo red color add
        except TypeError:
            print(f"TypeError")  # todo red color add

    return wrapper
