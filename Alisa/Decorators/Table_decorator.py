from tabulate import tabulate
from colorama import Fore


def table_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        headers = ["Id", "Name", "Company", "Email", "Birthday", "Address", "Phones", "Tags"]
        data = []
        for contact in result:
            data.append([
                contact.id_user,
                *(getattr(contact, attr).value if getattr(contact, attr) else "" for attr in
                  ["name", "company", "email", "birthday", "address"]),
                ", ".join([phone.value for phone in contact.phone]) if contact.phone else "",
                ", ".join([tag.value for tag in contact.tags]) if contact.tags else ""
            ])

        table = tabulate(data, headers=headers, tablefmt="grid")
        return Fore.LIGHTCYAN_EX + table

    return wrapper
