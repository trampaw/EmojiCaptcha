#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import random
from io import BytesIO

from PIL import Image

from emojicaptcha.emojis import supported_emojis, emojis_files
from emojicaptcha.types import Captcha

DATA_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)))
DEFAULT_BACKGROUND_PATH = os.path.join(DATA_DIR, "img/background.png")


class EmojiCaptcha:
    def __init__(self, background: str | None = None) -> None:
        """
        Initializes EmojiCaptcha.

        Args:
            background: Optional path to a background image for the captcha.
                        If None, uses DEFAULT_BACKGROUND_PATH.
        """
        self.background = background if background else DEFAULT_BACKGROUND_PATH

    @staticmethod
    def _generate_captcha_image(background_path: str, variants_count: int, data_dir: str) -> Captcha:
        """
        Generates the captcha image.
        """
        background = Image.open(background_path)
        image_obj = BytesIO()

        # Ensure variants_count is not None for range, default to 6 if None
        num_variants = variants_count if variants_count is not None else 6
        # Generate a list of random emoji characters (unicode)
        selected_emojis = [random.choice(supported_emojis) for _ in range(num_variants)]
        # Choose one of the selected emojis as the correct answer
        answer_emoji_char = random.choice(selected_emojis)
        # Get the file path for the answer emoji image
        answer_emoji_image_path = os.path.join(data_dir, emojis_files[answer_emoji_char])
        # Open the answer emoji image
        emoji_img = Image.open(answer_emoji_image_path)

        background.paste(
            im=emoji_img,  # Image to paste
            mask=emoji_img,  # Use alpha channel of emoji_img as mask for transparency
            box=(  # Center the emoji in the background
                background.size[0] // 2 - emoji_img.size[0] // 2,
                background.size[1] // 2 - emoji_img.size[1] // 2,
            ),
        )
        background.save(image_obj, "PNG", quality=100)
        return Captcha(image=image_obj, solution=answer_emoji_char, options=selected_emojis)

    def generate(self, variants_count: int | None = 6) -> Captcha:
        """
        Main function to Generate Captcha
        """
        return EmojiCaptcha._generate_captcha_image(
            background_path=self.background,
            variants_count=variants_count,
            data_dir=DATA_DIR  # Use the module-level DATA_DIR
        )

    @classmethod
    def get_captcha(cls, background_path: str | None = None, variants_count: int = 6) -> Captcha:
        """
        Generates a captcha without needing an instance of EmojiCaptcha.

        Args:
            background_path: Optional path to a background image. Uses default if None.
            variants_count: Number of emoji options to present. Defaults to 6.

        Returns:
            A Captcha object.
        """
        actual_background_path = (
            background_path if background_path else DEFAULT_BACKGROUND_PATH
        )
        return cls._generate_captcha_image( # Use cls for classmethod call
            background_path=actual_background_path,
            variants_count=variants_count,
            data_dir=DATA_DIR, # DATA_DIR is module level
        )


if __name__ == "__main__":
    # Get captcha using the new class method
    captcha_data = EmojiCaptcha.get_captcha()

    # Print some information
    # Note: The Captcha named tuple uses 'solution' for the answer and 'options' for the emoji list.
    print(f"Captcha solution: {captcha_data.solution}")
    print(f"Captcha options: {captcha_data.options}")

    # Save the image to a file
    captcha_data.image.seek(0)  # Reset stream position
    with open("example_captcha.png", "wb") as f:
        f.write(captcha_data.image.read())
    print("Example captcha image saved to example_captcha.png")

    # Optional: demonstrate with a custom background (using the default as an example)
    # This demonstrates passing the background argument, though it uses the same default.
    # For a true custom background, replace DEFAULT_BACKGROUND_PATH with an actual path to a different image.
    custom_bg_captcha_data = EmojiCaptcha.get_captcha(background_path=DEFAULT_BACKGROUND_PATH, variants_count=8)
    print(f"Custom BG Captcha solution: {custom_bg_captcha_data.solution}")
    print(f"Custom BG Captcha options: {custom_bg_captcha_data.options}")
    custom_bg_captcha_data.image.seek(0)
    with open("custom_example_captcha.png", "wb") as f:
        f.write(custom_bg_captcha_data.image.read())
    print("Custom background example captcha image saved to custom_example_captcha.png")
