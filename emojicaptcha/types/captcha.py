from io import BytesIO


class Captcha:

    def __init__(self, image: BytesIO, options: list[str], solution: str) -> None:
        self.image = image
        self.options = options
        self.solution = solution
