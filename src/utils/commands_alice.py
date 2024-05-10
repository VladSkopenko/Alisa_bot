from src.Bot.add import AliseAddContact
from src.Bot.delete import AlisaRemoveBot
from src.Bot.edit import AliseEditContact
from src.Bot.find import AliseFindContact
from src.Bot.qrb import AliseQR
from src.Bot.show_all import AliseShowAll
from src.Bot.help import AlisaHelp


commands = {
    "help": AlisaHelp,
    "add": AliseAddContact,
    "edit": AliseEditContact,
    "delete": AlisaRemoveBot,
    "find": AliseFindContact,
    "show": AliseShowAll,
    "qrb": AliseQR,
}
