import os

from functions import (
    coin_flip,
    emojify,
    hypotenuse,
    letter_grade,
    sorting_hat,
    weekly_pay
)
# -----main-----
if __name__ == '__main__':
    if os.getenv("UNIT_TEST"):
        # IGNORE THIS UNTIL YOU'VE FINISHED YOUR SUBMISSION, THEN YOU CAN TRY TO UNCOMMENT AND RUN THESE
        import unittest

        from test_coin_flip import TestCoinFlip
        from test_emoji import TestEmoji
        from test_hypotenuse import TestHypotenuse
        from test_letter_grade import TestLetterGrade
        from test_sorting_hat import TestSortingHat
        from test_weekly_pay import TestWeeklyPay

        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestSortingHat)
        suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestLetterGrade))
        suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestHypotenuse))
        suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestWeeklyPay))
        suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestCoinFlip))
        suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestEmoji))

        unittest.TextTestRunner().run(suite)
    else:
        print("What will I get?")
        for i in range(3):
            coin_flip()

        print()
        print("Can we do emojis?")
        print(emojify("pig"), emojify("pizza"))

        print("More complicated?")
        story = "Pig gave rhinoceros a balloon for his birthday. They ate pizza and were happy."
        emojied_story = ""
        for w in story.split(" "):
            emojied_story = emojied_story + emojify(w) + " "
        print(emojied_story)

        print()
        print("How about math?")
        print("sqrt(3^2 + 4^2) = {}".format(hypotenuse(3, 4)))
        print("How about with floats?")
        print("sqrt(6.4^2 + 9.3^2) = {:.2f}".format(hypotenuse(6.4, 9.3)))

        print()
        print("Sorting Hat? What's that?")
        for i in range(4):
            print(sorting_hat())

        print()
        print("With all of these, what's my pay?")
        print("If I worked 25 hours with $7.5/hr and I will get ${:.2f}/week".format(weekly_pay(25, 7.5)))
        print("But I actually worked 50 hours with $0/hr. So my pay is ${:.2f}. Sad".format(weekly_pay(50, 0)))

        print()
        print("No pay isn't a problem. Give me a grade.")
        print("My Grade is {}.".format(letter_grade(50)))
        print("You must be kidding me. My grade should be {}.".format(letter_grade(105)))