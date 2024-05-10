from abstract import AbstractBot
from src.models.record import Record
from src.utils.intro import help_alise


class HelpBot(AbstractBot):

    def handle(self, record: Record) -> None:
        help_alise()


AliceHelp = HelpBot()
