import unittest
from unittest.mock import Mock, patch, call

from main import (
    main,
    match_up
)


class MainLogic(unittest.TestCase):
    def test_matching(self):
        self.assertTrue(match_up("Romeo Montague", "Juliet Capulet"))

    def test_not_matching(self):
        self.assertFalse(match_up("Mickey Mouse", "Minnie Mouse"))

    # I tried, and failed
    # TODO: Complete unit tests for main()
    # @patch("main.input", side_effect=["Romeo Montague", "Juliet Capulet"])
    # @patch("main.print")
    # def test_main_matching(self, mock_input: Mock, mock_print: Mock):
    #     main()
    #     mock_input.assert_has_calls([
    #         call("Your name > "),
    #         call("Possible Soulmate > ")
    #     ])
    #     # mocked_print.assert_called_once_with("Possbile Soulmate > ")
    #     mock_print.assert_called_once_with("Romeo and Juliet are soulmates!")
    #
    #
    # @patch("main.print")
    # @patch("main.input", side_effect=["Mickey Mouse", "Minnie Mouse"])
    # def test_main_not_matching(self, mocked_print: Mock, mocked_input: Mock):
    #     main()
    #     mocked_print.assert_called_once_with("Your name > ")
    #     mocked_print.assert_called_once_with("Possbile Soulmate > ")
    #     mocked_print.assert_called_once_with("Mickey Mouse and Minnie Mouse are not destined to be together "
    #                                          "forever... :(")


if __name__ == '__main__':
    unittest.main()
