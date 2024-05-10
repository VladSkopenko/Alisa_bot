import cowsay


def introduce_alice():
    intro_text = f"""
    Hello! I am Alice!
    I am your personal assistant.
    I am here to help you!
    """
    cowsay.cow(text=intro_text)


def help_alice():
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
    exit_text = f"""
    Good bye!
    """
    cowsay.cow(text=exit_text)


if __name__ == "__main__":
    introduce_alice()
    help_alice()
    exit_alice()
