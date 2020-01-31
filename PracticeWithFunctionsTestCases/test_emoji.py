# YOU CAN IGNORE THIS FILE ENTIRELY

from unittest import TestCase

from functions import emojify


class TestEmoji(TestCase):
    def test_pig(self):
        self.assertEquals(
            emojify("pig"),
            '🐽'
        )

    def test_rhinocerous(self):
        try:
            self.assertEquals(
                emojify("rhinoceros"),
                '🦏'
            )
        except AssertionError as e:
            print(e)
            self.assertEquals(
                emojify("rhinoceros"),
                'rhinoceros'
            )

    def test_pizza(self):
        self.assertEquals(
            emojify("pizza"),
            '🍕'
        )

    def test_balloon(self):
        self.assertEquals(
            emojify("balloon"),
            '🎈'
        )
