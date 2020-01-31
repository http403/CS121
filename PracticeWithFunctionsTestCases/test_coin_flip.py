# YOU CAN IGNORE THIS FILE ENTIRELY

from unittest import TestCase
from unittest.mock import patch

from functions import coin_flip


class TestCoinFlip(TestCase):
    @patch('functions.print')
    def test_coin_flip(self, mock_print):
        coin_flip()
        try:
            mock_print.assert_called_with('Coin flip result is heads.')
        except AssertionError:
            mock_print.assert_called_with('Coin flip result is tails.')