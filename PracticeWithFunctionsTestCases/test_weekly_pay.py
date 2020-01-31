# YOU CAN IGNORE THIS FILE ENTIRELY

from unittest import TestCase

from functions import weekly_pay


class TestWeeklyPay(TestCase):
    def test_no_overtime(self):
        self.assertEquals(
            float(weekly_pay(10, 5.50)),
            55.0
        )

    def test_no_hours(self):
        self.assertEquals(
            float(weekly_pay(0, 5)),
            0.0
        )

    def test_40_hours(self):
        self.assertEquals(
            float(weekly_pay(40, 5)),
            200.0
        )

    def test_overtime(self):
        self.assertEquals(
            float(weekly_pay(50, 5)),
            275.0
        )

    def test_overtime_no_pay(self):
        self.assertEquals(
            float(weekly_pay(50, 0)),
            0.0
        )
