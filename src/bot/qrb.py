import uuid

import qrcode
from PIL import Image

from src.bot.abstract import AbstractBot


class QRBot(AbstractBot):

    def handle(self, link: str) -> None:
        """
        The handle function creates a QR code from the link provided.
        It saves it to a file and opens it in the default image viewer.

        :param self: Represent the instance of the class
        :param link: str: Pass the link that is to be converted into a qr code
        :return: None
        :doc-author: Trelent
        """
        if not link:
            link = input("Enter link: ")
        unique_id = uuid.uuid4()
        img = qrcode.make(link)
        img.save(f"Storage_QRcodes/{unique_id}.png")
        Image.open(f"Storage_QRcodes/{unique_id}.png").show()


AliceQR = QRBot()
