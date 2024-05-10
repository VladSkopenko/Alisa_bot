from abc import ABC
from abc import abstractmethod

from colorama import Fore

from src.address_book import AddressBook
from src.models.record import Record


class AbstractBot(ABC):
    def __init__(self):
        self.address_book = AddressBook()

    @abstractmethod
    def handle(self, *args):
        """
        The handle function is the main function of a management command.
        It's called by the Django framework when you run your command.


        :param self: Represent the instance of a class
        :param *args: Pass a variable number of arguments to the function
        :return: A string
        :doc-author: Trelent
        """
        pass

    @staticmethod
    def get_user_input_for_record_creation() -> Record:
        """
        The get_user_input_for_record_creation function prompts the user for input and returns a Record object.


        :return: A record object
        :doc-author: Trelent
        """
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
