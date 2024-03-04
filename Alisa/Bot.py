from abc import ABC, abstractmethod


class AbstractBot(ABC):
    def __init__(self, address_book: object):
        self.address_book = address_book

    @abstractmethod
    def handle(self):
        pass

    def exit(self):
        ...



class AddBot(AbstractBot):
    ...


class RemoveBot(AbstractBot):
    ...


class EditBot(AbstractBot):
    ...


class FindBot(AbstractBot):
    ...
