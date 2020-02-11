from random import randint
from typing import Callable


class Jukebox:
    """
    Ugly version of what I intended. Got limited by my knowledge and skill
    """
    _songs = {}

    def add_song(self, f: Callable) -> None:
        self._songs[f.__name__] = f

    # The main interface
    def run(self):
        selection = -1

        while selection != 8:
            if selection == 1:
                for i in range(3, 0, -1):
                    self._songs["frogs"](i)
            elif selection == 2:
                for i in range(10, 0, -1):
                    self._songs["monkeys"](i)
            elif selection == 3:
                for i in range(1, 13):
                    self._songs["hickory_dickory"](i)
            elif selection == 4:
                for i in range(100, 0, -10):
                    self._songs["milk"](i)
            elif selection == 5:
                climb = True
                while climb:
                    self._songs["spider"]()
                    if input("enter 'climb' to climb again > ").lower() != "climb":
                        climb = False
            elif selection == 6:
                ask = ""
                while ask.lower() != "no":
                    self._songs["abcs"]()
                    ask = input("(yes/no) > ")
            elif selection == 7:
                try:
                    while 1:
                        self._songs["song_never_ends"]()
                except KeyboardInterrupt:
                    pass

            selection = self._menu()

            if selection == 0:
                selection = randint(1, 6)

        print("🎵 Thanks for listening! 🎵")

    def _menu(self) -> int:
        print("====================================")
        print("0. I'm feeling lucky! (picks at random)")
        print("1. three speckled frogs")
        print("2. ten monkeys jumping on the bed")
        print("3. hickory dickory dock")
        print("4. 99 bottles of milk on the wall")
        print("5. itsy bitsy spider")
        print("6. ABCs")
        print("7. the song that never ends")
        print("8. NO MORE KID SONGS, PLEASE!")
        print("====================================\n")
        return int(input("Which nursery rhyme would you like to hear? > "))