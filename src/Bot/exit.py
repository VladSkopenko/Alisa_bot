from src.Bot.abstract import AbstractBot
from src.models.record import Record
from src.utils.intro import exit_alice


class ExitBot(AbstractBot):

    def handle(self, record: Record = None) -> None:
        exit_alice()


AliceExit = ExitBot()
