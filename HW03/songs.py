from jinja2 import Template


def farm(animal, sound):
    lyric = Template("""    Old MacDonald had a farm 
    e-i-e-i-o 
    And on that farm he had a {{animal}}
    e-i-e-i-o 
    With a {{sound}} {{sound}} here 
    And a {{sound}} {{sound}} there 
    Here a {{sound}}, there a {{sound}}
    Everywhere a {{sound}} {{sound}}
    Old MacDonald had a farm 
    e-i-e-i-o
    """)
    print(lyric.render(animal=animal, sound=sound))


def monkeys(number):
    lyric = Template("""    {{n}} little monkeys jumping on the bed 
    One fell off and bumped his head 
    Mama called the doctor, and the doctor said 
    "No more monkeys jumping on the bed!"
    """)
    print(lyric.render(n=number))


def hickory_dickory(time):
    lyric = Template("""    Hickory dickory dock 
    The mouse ran up the clock 
    The clock struck {{n}}
    The mouse ran down 
    Hickory dickory dock
    """)
    print(lyric.render(n=time))


def milk(number):
    lyric = Template("""    {{m}} bottles of milk on the wall
    {{m}} bottles of milk
    Take one down and pass it around
    {% if n > 0 %}{{n}} bottles of milk on the wall
    {% else %}No more bottles of milk on the wall
    {% endif %}
    """)
    print(lyric.render(m=number, n=number-1))


def hokey_pokey(body):
    lyric = Template("""    You put your {{body}} in
    You put your {{body}} out
    You put your {{body}} in
    And you shake it all about
    You do the Hokey Pokey
    And you turn yourself about
    That’s what it’s all about!
    """)
    print(lyric.render(body=body))


def forgs(number):
    lyric = Template("""    {{m}} little speckled frogs
    sitting on a speckled log
    eating the most delicious bugs
    yum, yum
    one jumped into the pool
    where it is nice and cool
    now there are {{n}} little speckled frogs!
    ribbit, ribbit
    """)
    print(lyric.render(m=number, n=number-1))