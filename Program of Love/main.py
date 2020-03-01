from time import sleep

import sys

def match_up(n1: str, n2: str) -> bool:
    counter: int = 0
    love: list = ['l', 'o', 'v', 'e']
    for c in love:
        counter += n1.lower().count(c)
        counter += n2.lower().count(c)
    if counter > 7:
        return True
    return False


def artificial_loading(time: float, factor: int = 10) -> None:
    time_divided: float = time / factor
    print("Checking", end="")
    for i in range(factor):
        # Weird behavior, print() will block with `end`; sys.stdout will output `.2` in WinPS and WSL
        # print(".\a", end="")
        sys.stdout.write(".\a")
        sys.stdout.flush()
        sleep(time_divided)
    print()


def main() -> None:
    n1: str = input("Your name > ")
    while True:
        n2: str = input("Possible Soulmate > ")
        print()
        artificial_loading(5)
        print()
        if match_up(n1, n2):
            print("{} and {} are soulmates!".format(n1.split()[0], n2.split()[0]))
            break
        print("{} and {} are not destined to be together forever... :(".format(n1, n2))


if __name__ == '__main__':
    main()