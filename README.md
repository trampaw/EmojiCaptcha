# ✨ emojicaptcha ✨

A simple, fast, and fun Python library to generate emoji-based captchas! 🛡️

## 📦 Installation

```bash
pip install emojicaptcha
```

## 🚀 Usage

The primary way to generate a captcha is by using the `EmojiCaptcha.get_captcha()` class method. This method returns a `Captcha` object with the following attributes:

*   `image`: A `BytesIO` object from the `io` module, containing the raw PNG image data. You can save this to a file or serve it directly in a web application.
*   `solution`: A string representing the correct emoji character that the user should identify.
*   `options`: A list of emoji characters (strings) that are presented to the user as choices, including the solution.

In a typical application, you would:
1.  Display the `image` to the user.
2.  Present the `options` (e.g., as clickable buttons or a dropdown).
3.  The user selects an emoji.
4.  Your application compares the user's selection with the `solution` to verify the captcha.

**Example 1.1: Basic Captcha Generation**

```python
from emojicaptcha import EmojiCaptcha
from emojicaptcha.types import Captcha # Good to show where Captcha comes from for type hinting
from io import BytesIO # For type hinting image attribute

# Generate a captcha
captcha_data: Captcha = EmojiCaptcha.get_captcha()

# The solution emoji
print(f"Solution: {captcha_data.solution}")

# The list of emoji options
print(f"Options: {captcha_data.options}")

# Save the captcha image
try:
    # captcha_data.image is a BytesIO object
    captcha_data.image.seek(0) # Go to the start of the BytesIO buffer
    with open("captcha_image.png", "wb") as f:
        f.write(captcha_data.image.read())
    print("Captcha image saved to captcha_image.png")
except Exception as e:
    print(f"Error saving image: {e}")
```
*(Example output might show an emoji for Solution and a list of emojis for Options)*

## ⚙️ Advanced Usage

You can customize the captcha generation with additional parameters.

**Example 2.1: Customizing Number of Emoji Options**

You can specify the number of emoji options (variants) to display.

```python
from emojicaptcha import EmojiCaptcha
from emojicaptcha.types import Captcha
from io import BytesIO

captcha_data: Captcha = EmojiCaptcha.get_captcha(variants_count=8) # Get 8 emoji options
print(f"Solution: {captcha_data.solution}")
print(f"Options (8): {captcha_data.options}")

# Save the image (similar to the basic example)
try:
    captcha_data.image.seek(0)
    with open("captcha_image_8_options.png", "wb") as f:
        f.write(captcha_data.image.read())
    print("Captcha image with 8 options saved to captcha_image_8_options.png")
except Exception as e:
    print(f"Error saving image: {e}")
```

**Example 2.2: Using a Custom Background Image**

You can provide a path to your own background image.

```python
from emojicaptcha import EmojiCaptcha
from emojicaptcha.types import Captcha
from io import BytesIO

# Ensure you have a background image, e.g., "my_background.png"
custom_bg_path = "path/to/your/custom_background.png" 

# Note: For this example to run, custom_bg_path must be a valid image file.
# If you don't have a custom background, this specific call will raise FileNotFoundError.
# For testing, you could use DEFAULT_BACKGROUND_PATH if imported from emojicaptcha.__main__

try:
    # captcha_data: Captcha = EmojiCaptcha.get_captcha(background_path=custom_bg_path)
    # print(f"Custom BG - Solution: {captcha_data.solution}")
    # captcha_data.image.seek(0)
    # with open("custom_bg_captcha.png", "wb") as f:
    #     f.write(captcha_data.image.read())
    # print(f"Captcha with custom background saved to custom_bg_captcha.png")
    print(f"Conceptual example: To use a custom background, provide its path to background_path.")
    print(f"Example: EmojiCaptcha.get_captcha(background_path='{custom_bg_path}')")
except FileNotFoundError:
    print(f"Error: Custom background image not found at {custom_bg_path}. Please provide a valid path.")
except Exception as e:
    print(f"An error occurred: {e}")
```

**Example 2.3: Using `EmojiCaptcha` Instance (Legacy/Alternative)**

While `get_captcha()` is recommended, you can also create an instance of `EmojiCaptcha` and call its `generate()` method. This might be useful if you want to reuse an instance with a specific configuration (e.g., a custom background) multiple times.

```python
from emojicaptcha import EmojiCaptcha
from emojicaptcha.types import Captcha
from io import BytesIO

# Instantiate the class (optionally with a custom background)
# For a custom background:
# emoji_captcha_instance = EmojiCaptcha(background="path/to/your/custom_background.png")
emoji_captcha_instance = EmojiCaptcha() # Uses default background

# Generate captcha using the instance
# You can also specify variants_count here
instance_captcha_data: Captcha = emoji_captcha_instance.generate(variants_count=5)

print(f"Instance - Solution: {instance_captcha_data.solution}")
print(f"Instance - Options (5): {instance_captcha_data.options}")

# Save the image (similar to the basic example)
try:
    instance_captcha_data.image.seek(0)
    with open("instance_captcha.png", "wb") as f:
        f.write(instance_captcha_data.image.read())
    print("Instance-generated captcha saved to instance_captcha.png")
except Exception as e:
    print(f"Error saving image: {e}")
```

## 🧪 Running Tests

To run the unit tests for this project, navigate to the root directory of the project in your terminal and execute the following command:

```bash
python -m unittest discover tests
```

This command will automatically discover and run all tests within the `tests` directory.

## 🤝 Contributing

Contributions are welcome! If you have ideas for improvements or find any issues, please open an issue or submit a pull request on the [GitHub repository](https://github.com/Jigarvarma2005/EmojiCaptcha).

## 🙏 Credits

-   [Jigar Varma(me😉)](https://github.com/JigarVarma2005)
-   [Abir Hasan](https://github.com/AbirHasan2005)
-   [Pillow](https://github.com/python-pillow/Pillow)
```
