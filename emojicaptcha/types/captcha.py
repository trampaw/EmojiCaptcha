from io import BytesIO


class Captcha:

    def __init__(self, image: BytesIO, emojis: list[str], answer: str) -> None:
        self.image = image
        self.emojis = emojis
        self.answer = answer
