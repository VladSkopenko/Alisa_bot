from src.utils.intro import introduce_alise
from src.utils.word_completer import word_completer
from src.utils.commands_alice import commands


class AlisaBot:
    intro = introduce_alise()
    word_completer = word_completer
    command = input(">>> ").lower()
    commands = commands

    def do_exit(self):
        if "exit" in self.command:
            print("Good Luck!")


if __name__ == "__main__":
    ...
