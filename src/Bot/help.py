from src.Bot.abstract import AbstractBot
from src.models.record import Record
from src.utils.intro import help_alice


class HelpBot(AbstractBot):

    def handle(self, record: Record = None) -> None:
        help_alice()


AliceHelp = HelpBot()
