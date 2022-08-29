#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import random
import uuid
from typing import List

from PIL import Image

from emojicaptcha.emojis import emojis_index, supported_emojis
from emojicaptcha.types import Captcha

DATA_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "emojis/img/")
try:
    os.mkdir("cache")
except OSError:
    pass


class EmojiCaptcha:
    def __init__(self, file_name: str = None, background: str = None) -> None:
        """
        Optional **args

        file_name[str]: custom file name for generating.

        background[str]: background image file path for captcha.
        """

        self.file_name = file_name if file_name else str(uuid.uuid4().hex)
        self.background = (
            background if background else os.path.join(DATA_DIR, "background.png")
        )

    def generate(self) -> Captcha:
        """
        Main function to Generate Captcha
        """
        background = Image.open(self.background)
        emojis: List[str] = list()
        r = random.random()
        random.shuffle(supported_emojis, lambda: r)
        for i in range(6):
            emojis.append(supported_emojis[i])
        captcha_answer = random.choice(emojis)
        captcha_image_path = os.path.join(
            DATA_DIR, emojis_index.get(captcha_answer) + ".png"
        )

        img = Image.open(captcha_image_path).rotate(
            random.randint(0, 360), resample=Image.BICUBIC, expand=True
        )
        img.thumbnail((200, 200), Image.ANTIALIAS)
        background.paste(img, (180, 160), img)
        captcha_image_path = os.path.join("cache", f"{self.file_name}.png")
        background.save(captcha_image_path, "PNG", quality=100)

        return Captcha(
            variants=emojis, answer=captcha_answer, file_path=captcha_image_path
        )
