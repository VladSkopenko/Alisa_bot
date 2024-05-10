from colorama import Fore
from tabulate import tabulate


def table_decorator(headers=None):
    """
    The table_decorator function is a decorator that takes in an optional list of headers.
    It then returns a decorator function that takes in the decorated function as its argument.
    The returned decorator function returns another wrapper function, which calls the decorated
    funciton and formats its output into a table using tabulate.

    :param headers: Specify the headers of the table
    :return: A decorator
    :doc-author: Trelent
    """

    def decorator(func):
        """
        The decorator function takes a function as an argument and returns a wrapper
            function. The wrapper function calls the original function, then formats
            the result into a table using tabulate.

        :param func: Pass the function that is being decorated
        :return: The wrapper function
        :doc-author: Trelent
        """

        def wrapper(*args, **kwargs):
            """
            The wrapper function is a decorator that takes the function as an argument and returns a new function.
            The wrapper function will print out the result of the decorated function in a table format using tabulate.

            :param *args: Pass a variable number of arguments to the function
            :param **kwargs: Pass keyworded, variable-length argument list to the function
            :return: The tabulated result in a nice format
            :doc-author: Trelent
            """
            result = func(*args, **kwargs)
            if headers:
                table = tabulate(result, headers=headers, tablefmt="grid")
            else:
                table = tabulate(result, headers="keys", tablefmt="grid")
            return Fore.LIGHTCYAN_EX + table

        return wrapper

    return decorator
