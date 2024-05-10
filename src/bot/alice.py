from src.bot.exit import AliceExit
from src.utils.intro import introduce_alice
from src.bot.add import AliceAddContact
from src.bot.delete import AliceRemoveBot
from src.bot.edit import AliceEditContact
from src.bot.find import AliceFindContact
from src.bot.qrb import AliceQR
from src.bot.show_all import AliceShowAll
from src.bot.help import AliceHelp


class AlisaBot:
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

    def run_bot(self):
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
                user_name = input("Enter name: ").lower()
                new_contact = AliceEditContact.get_user_input_for_record_creation()
                self.handler[user_command](user_name, new_contact)

            elif user_command == "delete":
                user_id = input("Enter ID: ")
                self.handler[user_command](user_id)

            elif user_command == "find":
                user_name = input("Enter name: ").lower()
                self.handler[user_command](user_name)
            elif user_command == "qr":

                link = input("Enter link: ")
                self.handler[user_command](link)

            elif user_command == "show":
                self.handler[user_command]()

            else:
                self.handler["help"]()


MainBot = AlisaBot()