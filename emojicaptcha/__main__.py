#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import random
from io import BytesIO

from PIL import Image

from emojicaptcha.emojis import supported_emojis, emojis_files
from emojicaptcha.types import Captcha

DATA_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "img/")
try:
    os.mkdir("cache")
except OSError:
    pass


class EmojiCaptcha:
    def __init__(self, background: str = None) -> None:
        """
        Optional **args

        background[str]: background image file path for captcha.
        """

        # self.file_name = file_name if file_name else str(uuid.uuid4().hex)
        self.background = (
            background if background else os.path.join(DATA_DIR, "background.png")
        )

    def generate(self, variants_count: int | None = 6) -> Captcha:
        """
        Main function to Generate Captcha
        """
        background = Image.open(self.background)

        image_obj = BytesIO()

        emojis = [random.choice(supported_emojis) for _ in range(variants_count)]
        answer = random.choice(emojis)
        emoji = Image.open(os.path.join(emojis_files[answer]))
        background.paste(
            im=emoji,
            mask=emoji,
            box=(
                background.size[0]//2 - emoji.size[0]//2,
                background.size[1]//2 - emoji.size[1]//2
            )
        )
        background.save(image_obj, "PNG", quality=100)

        return Captcha(image_obj, emojis, answer)


if __name__ == "__main__":
    captcha = EmojiCaptcha()
    captcha.generate()
