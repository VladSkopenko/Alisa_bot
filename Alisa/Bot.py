from abc import ABC, abstractmethod
from models.record import Record
from Address_book import ADDRESSBOOK
from Connect_db import update_db

class AbstractBot(ABC):
    def __init__(self):
        self.address_book = ADDRESSBOOK

    @abstractmethod
    def handle(self):
        pass


class AddBot(AbstractBot):
    def __init__(self):
        super().__init__()

    def handle(self, record: Record) -> None:
        update_db(record)



class RemoveBot(AbstractBot):
    ...


class EditBot(AbstractBot):
    ...


class FindBot(AbstractBot):
    ...


if __name__ == "__main__":
    ad = AddBot()
    per = Record(name="Vlad",
                 phone="380961630573",
                 tag="student",
                 email="exsam@fa.com",
                 birthday="2000-01-28",
                 company="go it",
                 address="address231213"
                 )
    ad.handle(per)


