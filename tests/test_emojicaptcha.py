import unittest
from io import BytesIO
import os

# Attempt to import EmojiCaptcha and Captcha from the main package
# This might require adjusting the Python path when running tests,
# but for now, assume the tests will be run from the project root.
from emojicaptcha import EmojiCaptcha
from emojicaptcha.types import Captcha
# DEFAULT_BACKGROUND_PATH is used for a valid background test case
from emojicaptcha.__main__ import DEFAULT_BACKGROUND_PATH, DATA_DIR

# Ensure supported_emojis is available for some tests if needed, or that tests don't rely on its internal structure
from emojicaptcha.emojis import supported_emojis

class TestEmojiCaptcha(unittest.TestCase):

    def test_get_captcha_default(self):
        """Test get_captcha with default parameters."""
        captcha_data = EmojiCaptcha.get_captcha()
        self.assertIsInstance(captcha_data, Captcha)
        self.assertIsInstance(captcha_data.image, BytesIO)
        self.assertTrue(len(captcha_data.image.getvalue()) > 0)
        self.assertIsInstance(captcha_data.solution, str)
        self.assertIn(captcha_data.solution, captcha_data.options)
        self.assertIsInstance(captcha_data.options, list)
        self.assertEqual(len(captcha_data.options), 6) # Default variants count

    def test_get_captcha_variants_count(self):
        """Test get_captcha with different variants_count."""
        captcha_data_8 = EmojiCaptcha.get_captcha(variants_count=8)
        self.assertIsInstance(captcha_data_8, Captcha)
        self.assertEqual(len(captcha_data_8.options), 8)
        self.assertIn(captcha_data_8.solution, captcha_data_8.options)

        captcha_data_4 = EmojiCaptcha.get_captcha(variants_count=4)
        self.assertIsInstance(captcha_data_4, Captcha)
        self.assertEqual(len(captcha_data_4.options), 4)
        self.assertIn(captcha_data_4.solution, captcha_data_4.options)

    def test_get_captcha_custom_background_valid(self):
        """Test get_captcha with a valid custom background path."""
        # We use DEFAULT_BACKGROUND_PATH as a known valid background
        captcha_data = EmojiCaptcha.get_captcha(background_path=DEFAULT_BACKGROUND_PATH)
        self.assertIsInstance(captcha_data, Captcha)
        self.assertIsInstance(captcha_data.image, BytesIO)
        self.assertTrue(len(captcha_data.image.getvalue()) > 0)
        self.assertIn(captcha_data.solution, captcha_data.options)

    def test_get_captcha_custom_background_invalid(self):
        """Test get_captcha with an invalid (non-existent) custom background path."""
        with self.assertRaises(FileNotFoundError):
            EmojiCaptcha.get_captcha(background_path="non_existent_background.png")

    def test_instance_generate_default_background(self):
        """Test instance generate() with default background (from __init__)."""
        captcha_instance = EmojiCaptcha()
        captcha_data = captcha_instance.generate()
        self.assertIsInstance(captcha_data, Captcha)
        self.assertIsInstance(captcha_data.image, BytesIO)
        self.assertTrue(len(captcha_data.image.getvalue()) > 0)
        self.assertIsInstance(captcha_data.solution, str)
        self.assertIn(captcha_data.solution, captcha_data.options)
        self.assertEqual(len(captcha_data.options), 6) # Default variants

    def test_instance_generate_custom_background_init(self):
        """Test instance generate() with custom background set in __init__."""
        # Using DEFAULT_BACKGROUND_PATH as a known valid background
        captcha_instance = EmojiCaptcha(background=DEFAULT_BACKGROUND_PATH)
        captcha_data = captcha_instance.generate()
        self.assertIsInstance(captcha_data, Captcha)
        self.assertIsInstance(captcha_data.image, BytesIO)
        self.assertTrue(len(captcha_data.image.getvalue()) > 0)
        self.assertIn(captcha_data.solution, captcha_data.options)

    def test_instance_generate_variants_count(self):
        """Test instance generate() with a custom variants_count."""
        captcha_instance = EmojiCaptcha()
        captcha_data = captcha_instance.generate(variants_count=5)
        self.assertIsInstance(captcha_data, Captcha) # Added for completeness
        self.assertEqual(len(captcha_data.options), 5)
        self.assertIn(captcha_data.solution, captcha_data.options)

if __name__ == '__main__':
    unittest.main()
