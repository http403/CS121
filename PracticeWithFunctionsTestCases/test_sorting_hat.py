# YOU CAN IGNORE THIS FILE ENTIRELY

from unittest import TestCase

from functions import sorting_hat


class TestSortingHat(TestCase):
    def test_sorting_hat(self):
        self.assertIn(
            sorting_hat(),
            [
                "Gryffindor",
                "Hufflepuff",
                "Ravenclaw",
                "Slytherin"
            ]
        )
