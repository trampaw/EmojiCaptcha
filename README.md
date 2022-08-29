# emojicaptcha

# Installation
------------

Install emojicaptcha with pip::

    $ pip install emojicaptcha

# Usage
------------

``` python
from emojicaptcha import EmojiCaptcha

captcha = EmojiCaptcha()
"""
    Optional **args

    file_name[str]: custom file name for generating.

    background[str]: background image file path for captcha.

    ---------------------------------------------------------

    Return type -----> Captcha
    """
#Generate captcha
generated_captcha = captcha.generate()

#Print the output
print(generated_captcha)
```

**emojicaptcha** is Fast, Easy python3 library to generate Emoji captcha.

#### Credits
- [Jigar Varma(me😉)](https://github.com/JigarVarma2005)
- [Abir Hasan](https://github.com/AbirHasan2005)
- [Pillow](https://github.com/python-pillow/Pillow)
