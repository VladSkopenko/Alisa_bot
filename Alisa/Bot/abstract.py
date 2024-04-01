from abc import ABC, abstractmethod

from Alisa.models.record import Record
from Alisa.Address_book import AddressBook


class AbstractBot(ABC):
    def __init__(self):
        self.address_book = AddressBook()

    @abstractmethod
    def handle(self, *args):
        pass

    @staticmethod
    def get_user_input_for_record_creation() -> Record:
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        tag = input("Enter tag: ")
        email = input("Enter email: ")
        birthday = input("Enter birthday (YYYY-MM-DD): ")
        company = input("Enter company: ")
        address = input("Enter address: ")

        record = Record(
            name=name,
            phone=phone,
            tag=tag,
            email=email,
            birthday=birthday,
            company=company,
            address=address
        )
        return record
