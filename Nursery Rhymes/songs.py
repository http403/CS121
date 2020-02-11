from jukebox import Jukebox

jukebox = Jukebox()


# TODO: use decorator instead of direct function call to Jukebox.add_song() method

def frogs(number: int) -> None:
    print(number, "little speckled frogs")
    print("sitting on a speckled log")
    print("eating the most delicious bugs")
    print("yum, yum")
    print("one jumped into the pool")
    print("where it is nice and cool")
    print("now there are", number - 1, "little speckled frogs!")
    print("ribbit, ribbit")
    print()
jukebox.add_song(frogs)


def monkeys(number: int) -> None:
    print(number, "little monkeys jumping on the bed")
    print("One fell off and bumped his head")
    print("Mama called the doctor, and the doctor said")
    print('"No more monkeys jumping on the bed!"')
    print()
jukebox.add_song(monkeys)


def hickory_dickory(time: int) -> None:
    print("Hickory dickory dock")
    print("The mouse ran up the clock")
    print("The clock struck", time)
    print("The mouse ran down")
    print("Hickory dickory dock")
    print()
jukebox.add_song(hickory_dickory)


def milk(number: int) -> None:
    print(number, "bottles of milk on the wall")
    print(number, "bottles of milk")
    print("Take TEN down and pass it around")
    print("No" if number - 10 > 0 else number - 10, "bottles of milk on the wall")
    print()
jukebox.add_song(milk)


def spider():
    print("The itsy bitsy spider climbed up the waterspout.")
    print("Down came the rain")
    print("and washed the spider out.")
    print()
    print("Out came the sun")
    print("and dried up all the rain")
    print("and the itsy bitsy spider climbed up the spout again.")
jukebox.add_song(spider)


def abcs():
    print("""ABCD, EFG,
HIJK, LMNOP
QRS, TUV
WX, Y and Z
Now I know my ABCs,
Next time won't you sing with me?""")
jukebox.add_song(abcs)


def song_never_ends():
    print("""This is the song that never ends.
It goes on and on my friends.
Some people started singing it
not knowing what it was.
And now they are still singing it
forever just because...""")
jukebox.add_song(song_never_ends)