import uuid

import qrcode
from PIL import Image

from abstract import AbstractBot


class QRBot(AbstractBot):

    def handle(self, link: str) -> None:
        """
        Creates qrcode
        """
        unique_id = uuid.uuid4()
        img = qrcode.make(link)
        img.save(f"Storage_QRcodes/{unique_id}.png")
        Image.open(f"Storage_QRcodes/{unique_id}.png").show()


if __name__ == "__main__":
    q = QRBot()
    q.handle("https://github.com/LudSkop")
