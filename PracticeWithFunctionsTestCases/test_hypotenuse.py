# YOU CAN IGNORE THIS FILE ENTIRELY

from unittest import TestCase

from functions import hypotenuse


class TestHypotenuse(TestCase):
    def test_hypotenuse(self):
        self.assertAlmostEqual(
            hypotenuse(4, 5), 6.4, places=1
        )
