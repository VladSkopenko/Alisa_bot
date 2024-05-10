import cmd
from prompt_toolkit import prompt
from src.utils.intro import introduce_alise
from rich.console import Console
from src.Bot.add import AddBot
from src.Bot.delete import RemoveBot
from src.Bot.edit import EditBot
from src.Bot.find import FindBot
from src.Bot.qrb import QRBot


class AlisaBot(cmd.Cmd):
    intro = introduce_alise()
    console = Console()
