# YOU CAN IGNORE THIS FILE ENTIRELY

from unittest import TestCase

from functions import letter_grade


class TestLetterGrade(TestCase):
    def test_letter_grade_100(self):
        self.assertEqual(
            letter_grade(100), "A"
        )

    def test_letter_grade_95(self):
        self.assertEqual(
            letter_grade(95), "A"
        )

    def test_letter_grade_90(self):
        self.assertEqual(
            letter_grade(90), "A"
        )

    def test_letter_grade_89(self):
        self.assertEqual(
            letter_grade(89), "B"
        )

    def test_letter_grade_80(self):
        self.assertEqual(
            letter_grade(80), "B"
        )

    def test_letter_grade_79(self):
        self.assertEqual(
            letter_grade(79), "C"
        )

    def test_letter_grade_67(self):
        self.assertEqual(
            letter_grade(67), "C"
        )

    def test_letter_grade_66(self):
        self.assertEqual(
            letter_grade(66), "F"
        )

    def test_letter_grade_0(self):
        self.assertEqual(
            letter_grade(0), "F"
        )
