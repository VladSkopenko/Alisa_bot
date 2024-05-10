from src.bot.add import AliceAddContact
from src.bot.delete import AliceRemoveBot
from src.bot.edit import AliceEditContact
from src.bot.exit import AliceExit
from src.bot.find import AliceFindContact
from src.bot.help import AliceHelp
from src.bot.qrb import AliceQR
from src.bot.show_all import AliceShowAll
from src.decorators.error_handler import error_handler
from src.utils.intro import introduce_alice


class AlisaBot:
    def __init__(self):
        self.handlers = {
            "add": self.handle_add,
            "delete": self.handle_delete,
            "edit": self.handle_edit,
            "find": self.handle_find,
            "help": self.handle_help,
            "qr": self.handle_qr,
            "show": self.handle_show,
        }
        introduce_alice()

    @error_handler
    def run(self):
        """
        The run function is the main loop of the program. It will continue to run until
        the user enters 'exit' as a command. The function takes in user input and checks if it matches any of
        the commands listed in self.handlers, which are all functions that have been defined above (handle_help, handle_list, etc.). If there is no match for the command entered by the user then it will print out a help message with all available commands.

        :param self: Keep a reference to the current instance of the class, and is used to access variables that belongs to the class
        :return: None
        :doc-author: Trelent
        """
        while True:
            user_command = input("Enter command: ").lower()
            if user_command == "exit":
                self.handle_exit()
                break
            elif user_command in self.handlers:
                self.handlers[user_command]()
            else:
                self.handle_help()

    @staticmethod
    def handle_add():
        AliceAddContact.handle()

    @staticmethod
    def handle_delete():
        AliceRemoveBot.handle()

    @staticmethod
    def handle_edit():
        AliceEditContact.handle()

    @staticmethod
    def handle_find():
        AliceFindContact.handle()

    @staticmethod
    def handle_help():
        AliceHelp.handle()

    @staticmethod
    def handle_qr():
        AliceQR.handle()

    @staticmethod
    def handle_show():
        AliceShowAll.handle()

    @staticmethod
    def handle_exit():
        AliceExit.handle()


bot = AlisaBot()
