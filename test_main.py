import unittest

from main import SPACE, decode, encode


class CipherTests(unittest.TestCase):
    def test_round_trip_ascii_and_unicode(self):
        samples = (
            "",
            "Hello, world!",
            "مرحبا بالعالم",
            "Emoji: 😀",
            "\uD7FF",
            "\uE000",
            "\U0010FFFF",
        )

        for text in samples:
            with self.subTest(text=text):
                ciphertext = encode(text, key=5)
                self.assertEqual(decode(ciphertext, key=5), text)
                self.assertTrue(
                    all(not 0xD800 <= ord(char) <= 0xDFFF for char in ciphertext)
                )

    def test_existing_shift_behavior_for_ascii(self):
        text = "abc"
        expected = "".join(chr(ord(char) + SPACE + 4) for char in text)
        self.assertEqual(encode(text), expected)

    def test_rejects_surrogate_input(self):
        with self.assertRaisesRegex(ValueError, "surrogate"):
            encode("\uD800")

        with self.assertRaisesRegex(ValueError, "surrogate"):
            decode("\uDFFF")


if __name__ == "__main__":
    unittest.main()
