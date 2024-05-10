from prompt_toolkit.completion import WordCompleter

word_completer = WordCompleter(
    [
        "help",
        "exit",
        "add_contact",
        "edit_contact",
        "delete_contact",
        "show_all_contacts",
        "find_contact",
        "create_qr_code",
    ]
)
