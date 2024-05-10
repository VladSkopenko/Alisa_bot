from colorama import Fore


def error_handler(func):
    """
    The error_handler function is a decorator that wraps the function it's applied to.
    It catches any exceptions raised by the wrapped function and returns them as strings,
    instead of raising them. This allows us to use functions like get_user_input() in our
    main program without having to worry about catching errors.

    :param func: Pass the function that will be decorated
    :return: The result of the function if there is no error,
    :doc-author: Trelent
    """

    def wrapper(*args, **kwargs):
        """
        The wrapper function is a decorator that wraps the function passed to it.
        It catches any exceptions raised by the wrapped function and returns them as strings in red text.

        :param *args: Send a non-keyworded variable length argument list to the function
        :param **kwargs: Pass keyworded, variable-length argument list to the function
        :return: The result of the function
        :doc-author: Trelent
        """
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            return Fore.LIGHTRED_EX + str(e)

    return wrapper
