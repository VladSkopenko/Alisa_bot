from abc import ABC
from abc import abstractmethod

from colorama import Fore

from src.Address_book import AddressBook
from src.models.record import Record


class AbstractBot(ABC):
    def __init__(self):
        self.address_book = AddressBook()

    @abstractmethod
    def handle(self, *args):
        pass

    @staticmethod
    def get_user_input_for_record_creation() -> Record:
        name = input(Fore.BLUE + "Enter name: ")
        phone = input(Fore.GREEN + "Enter phone number: ")
        tag = input(Fore.LIGHTRED_EX + "Enter tag: ")
        email = input(Fore.MAGENTA + "Enter email: ")
        birthday = input(Fore.LIGHTCYAN_EX + "Enter birthday (YYYY-MM-DD): ")
        company = input(Fore.RESET + "Enter company: ")
        address = input(Fore.LIGHTYELLOW_EX + "Enter address: ")

        record = Record(
            name=name,
            phone=phone,
            tag=tag,
            email=email,
            birthday=birthday,
            company=company,
            address=address,
        )
        return record
