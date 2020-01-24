from jinja2 import Template

inputs = {}

plot = Template("""RLCraft modded Minecraft > New Game

Spawns in the middle of the {{ time_of_day }}. Surrounded by {{ number }} {{ mobs }}. Dead.
Respwan. A giant {{ color }} dragon showed up and got {{ food_texture }} like a {{ fried_food }}.
Enough, close the game and get to {{ sad_activity }}.

Next day. Opened the game and decided to give it another try.
Spwans in. {{ pos_emo_noun }}, safe. Get started to obtaining {{ mc_block_rich }} but what?
Nothing. I can't mine! Oh, I need to dig some {{ mc_block_rare }} first. But look around, in the middle of a {{ mc_landscape }}.

On the way to find {{ mc_block_rare }} but got surrounded by {{ mobs }}, again. Dead.
{{ neg_emo_phrase }}! Close game and never touch it again.

P.S. Real Story
""")


def compose(inputs):
    """
    Replace placeholders in the plot template

    :param inputs: A dict contains every placeholders
    :return: The rendered plot
    """
    return plot.render(
        **inputs
    )  # Unpack the dict into individual variable named by their key


def askinput(prompt, desired_type="str"):
    """
    A custom implementation of input() to achieve type conversion and checking

    :param prompt: As the prompt will be output by input()
    :param desired_type: Either "str" or "int", used in type conversion
    :return: The input with desired type
    """
    if desired_type == "str":
        out = input(prompt)
        return out.upper()
    elif desired_type == "int":
        valid = False
        while not valid:
            try:
                out = int(input(prompt))
                valid = True
            except ValueError:
                print("Not a number.")
        return out
    else:
        print("Invalid Type")


if __name__ == "__main__":
    print("Welcome to my MadLib program.\n")

    print("Please provide the info below:")
    inputs['time_of_day'] = askinput(
        "Specify a time of day (day, noon, night) > ")
    inputs['number'] = askinput("A number > ", "int")
    inputs['color'] = askinput("Your favorite color > ")
    inputs['fried_food'] = askinput("A fried food you love > ")
    inputs['food_texture'] = askinput("Describe that food in past tense > ")
    inputs['pos_emo_noun'] = askinput("A positive emotion noun > ")
    inputs['neg_emo_phrase'] = askinput("A negative emotion phrase > ")
    inputs['sad_activity'] = askinput("What you do when you feel sad? > ")
    inputs['mc_landscape'] = askinput("A Minecraft landscape > ")
    inputs['mc_block_rich'] = askinput(
        "A Minecraft block rich in your landscape (wood, stone, etc) > ")
    inputs['mc_block_rare'] = askinput(
        "A Minecraft block rare in you landscape (wood, stone, etc) > ")
    inputs['mobs'] = askinput("A Minecraft mob you most scared of > ")

    print("\n---\n")
    print(compose(inputs))

"""
Welcome to my MadLib program.

Please provide the info below:
Specify a time of day (day, noon, night) > night
A number > 9
Your favorite color > green
A fried food you love > fried chicken
Describe that food in past tense > crisped
A positive emotion noun > hell yeah
A negative emotion phrase > god damn it
What you do when you feel sad? > sleep
A Minecraft landscape > forest
A Minecraft block rich in your landscape (wood, stone, etc) > wood
A Minecraft block rare in you landscape (wood, stone, etc) > gravel
A Minecraft mob you most scared of > creeper

---

RLCraft modded Minecraft > New Game

Spawns in the middle of the NIGHT. Surrounded by 9 CREEPER. Dead.
Respwan. A giant GREEN dragon showed up and got CRISPED like a FRIED CHICKEN.
Enough, close the game and get to SLEEP.

Next day. Opened the game and decided to give it another try.
Spwans in. HELL YEAH, safe. Get started to obtaining WOOD but what?
Nothing. I can't mine! Oh, I need to dig some GRAVEL first. But look around, in the middle of a FOREST.

On the way to find GRAVEL but got surrounded by CREEPER, again. Dead.
GOD DAMN IT! Close game and never touch it again.

P.S. Real Story
"""
