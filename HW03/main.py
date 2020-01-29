from songs import (
    farm,
    hickory_dickory,
    monkeys as monkey,
    milk,
    hokey_pokey,
    forgs as forg,
)


# Define some constants
milk_bottle = 10
animals = {
    "cow": "moo",
    "duck": "quack",
    "chicks": "cluck"
}

bodies = [
    "right arm",
    "left leg"
]

monkeys = {
    # start > end
    "start": 10,
    "end": 8
}

clock = {
    # start < end
    "start": 1,
    "end": 3
}

forgs = {
    # start > end
    "start": 3,
    "end": 2
}

if __name__ == '__main__':
    # A loop to ask how many milk bottles we have
    valid = False
    while not valid:
        try:
            milk_bottle = int(input("How many bottles of milk are there? > "))
            if milk_bottle is not None:
                valid = True
        except ValueError:
            print("Not a number")

    for animal, sound in animals.items():
        farm(animal, sound)

    for i in range(monkeys["start"],monkeys["end"],-1):
        monkey(i)

    for i in range(clock["start"], clock["end"]):
        hickory_dickory(i)

    for body in bodies:
        hokey_pokey(body)

    for i in range(forgs["start"], forgs["end"], -1):
        forg(i)

    for i in range(milk_bottle, 0, -1):
        milk(i)

"""
How many bottles of milk are there? > 2
    Old MacDonald had a farm 
    e-i-e-i-o 
    And on that farm he had a cow
    e-i-e-i-o 
    With a moo moo here 
    And a moo moo there 
    Here a moo, there a moo
    Everywhere a moo moo
    Old MacDonald had a farm 
    e-i-e-i-o
    
    Old MacDonald had a farm 
    e-i-e-i-o 
    And on that farm he had a duck
    e-i-e-i-o 
    With a quack quack here 
    And a quack quack there 
    Here a quack, there a quack
    Everywhere a quack quack
    Old MacDonald had a farm 
    e-i-e-i-o
    
    Old MacDonald had a farm 
    e-i-e-i-o 
    And on that farm he had a chicks
    e-i-e-i-o 
    With a cluck cluck here 
    And a cluck cluck there 
    Here a cluck, there a cluck
    Everywhere a cluck cluck
    Old MacDonald had a farm 
    e-i-e-i-o
    
    10 little monkeys jumping on the bed 
    One fell off and bumped his head 
    Mama called the doctor, and the doctor said 
    "No more monkeys jumping on the bed!"
    
    9 little monkeys jumping on the bed 
    One fell off and bumped his head 
    Mama called the doctor, and the doctor said 
    "No more monkeys jumping on the bed!"
    
    Hickory dickory dock 
    The mouse ran up the clock 
    The clock struck 1
    The mouse ran down 
    Hickory dickory dock
    
    Hickory dickory dock 
    The mouse ran up the clock 
    The clock struck 2
    The mouse ran down 
    Hickory dickory dock
    
    You put your right arm in
    You put your right arm out
    You put your right arm in
    And you shake it all about
    You do the Hokey Pokey
    And you turn yourself about
    That’s what it’s all about!
    
    You put your left leg in
    You put your left leg out
    You put your left leg in
    And you shake it all about
    You do the Hokey Pokey
    And you turn yourself about
    That’s what it’s all about!
    
    3 little speckled frogs
    sitting on a speckled log
    eating the most delicious bugs
    yum, yum
    one jumped into the pool
    where it is nice and cool
    now there are 2 little speckled frogs!
    ribbit, ribbit
    
    2 bottles of milk on the wall
    2 bottles of milk
    Take one down and pass it around
    1 bottles of milk on the wall
    
    
    1 bottles of milk on the wall
    1 bottles of milk
    Take one down and pass it around
    No more bottles of milk on the wall
"""