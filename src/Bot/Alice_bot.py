from prompt_toolkit import PromptSession

from Bot.exit import AliceExit
from utils.intro import introduce_alice
from utils.word_completer import word_completer
from common.reqular_exp import EXIT
from src.Bot.add import AliceAddContact
from src.Bot.delete import AliceRemoveBot
from src.Bot.edit import AliceEditContact
from src.Bot.find import AliceFindContact
from src.Bot.qrb import AliceQR
from src.Bot.show_all import AliceShowAll
from src.Bot.help import AliceHelp


class AlisaBot:
    word_completer = word_completer
    handler = {
        "help": AliceHelp.handle,
        "add": AliceAddContact.handle,
        "edit": AliceEditContact.handle,
        "delete": AliceRemoveBot.handle,
        "find": AliceFindContact.handle,
        "show": AliceShowAll.handle,
        "qr": AliceQR.handle,
        "exit": AliceExit.handle,
    }

    def do_start(self):
        introduce_alice()

        while True:
            user_command = input(">>> ").lower()
            if user_command == "exit":
                self.handler["exit"]()
                break
            elif user_command == "add":
                new_contact = AliceAddContact.get_user_input_for_record_creation()
                self.handler[user_command](new_contact)

            elif user_command == "edit":
                user_name = input("Enter name: ")
                new_contact = AliceEditContact.get_user_input_for_record_creation()
                self.handler[user_command](user_name, new_contact)

            elif user_command == "delete":
                user_id = input("Enter ID: ")
                self.handler[user_command](user_id)

            elif user_command == "find":
                user_name = input("Enter name: ")
                self.handler[user_command](user_name)
            elif user_command == "qr":

                link = input("Enter link: ")
                self.handler[user_command](link)

            elif user_command == "show":
                self.handler[user_command]()

            else:
                self.handler["help"]()


if __name__ == "__main__":
    a = AlisaBot()
    a.do_start()
