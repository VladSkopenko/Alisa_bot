import cowsay


def introduce_alice():
    """
    The introduce_alice function prints a friendly introduction to the user.

    :return: A cowsay
    :doc-author: Trelent
    """
    intro_text = f"""
    Hello! I am Alice!
    I am your personal assistant.
    I am here to help you!
    """
    cowsay.cow(text=intro_text)


def help_alice():
    """
    The help_alice function prints out a list of commands that the user can use to interact with their address book.

    :return: The help_text variable
    :doc-author: Trelent
    """
    help_text = f"""
    I can help you with the following commands with your address book:
    - add contact(add)
    - delete contact(delete)
    - edit contact(edit)
    - find contact(find)
    - show all contacts(show)
    - create_qr_code (qr)
    - exit
    """
    cowsay.cow(text=help_text)


def exit_alice():
    """
    The exit_alice function is a simple function that prints out a goodbye message to the user.


    :return: The exit_text string
    :doc-author: Trelent
    """
    exit_text = f"""
    Good bye!
    """
    cowsay.cow(text=exit_text)
