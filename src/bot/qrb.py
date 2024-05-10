import uuid

import qrcode
from PIL import Image

from src.bot.abstract import AbstractBot


class QRBot(AbstractBot):

    def handle(self, link: str) -> None:
        """
        Creates qrcode
        """
        unique_id = uuid.uuid4()
        img = qrcode.make(link)
        img.save(f"Storage_QRcodes/{unique_id}.png")
        Image.open(f"Storage_QRcodes/{unique_id}.png").show()


AliceQR = QRBot()
