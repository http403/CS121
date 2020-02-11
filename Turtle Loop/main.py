import turtle
import random


def draw_square(t, side):
    for i in range(4):
        t.forward(side)
        t.right(90)


def four_square(t, side):
    # You already have the code to draw a square above
    # So you can use a loop to call the function
    # and then set your turtle's heading
    for i in range(4):
        draw_square(t, side/2)
        t.left(90)


def six_petal_flower(t, side):
    for i in range(6):
        draw_square(t, side)
        t.left(60)


def twelve_petal_flower(t, side):
    for i in range(12):
        draw_square(t, side)
        t.left(30)


def draw_triangle(t, side):
    for i in range(3):
        t.forward(side)
        t.left(120)


def draw_hexagon(t, side):
    for i in range(6):
        t.forward(side)
        t.left(60)


def basic_spiral(t, n, side):
    for i in range(n):
        draw_square(t, side*i)
        t.left(30)


def color_spiral(t, n, side, screen):
    for i in range(n+1):
        screen.title("Drawing {} of {} squares".format(i, n))
        t.color(random.choice(['red', 'blue']))
        draw_square(t, side*i)
        t.left(30)


def color_triangle_spiral(t, n, side, screen):
    for i in range(n+1):
        screen.title("Drawing {} of {} triangles".format(i, n))
        t.color(random.choice(['red', 'blue']))
        draw_triangle(t, side*i)
        t.left(30)


# ======main======
if __name__ == '__main__':
    wn = turtle.Screen()
    wn.bgcolor("#646464")
    # wn.mode("logo")
    wn.listen()

    my_turtle = turtle.Turtle()
    my_turtle.shape("turtle")
    # my_turtle.speed(3)
    my_turtle.color("#FFFFFF")

    # draw_square(my_turtle, 100)
    # four_square(my_turtle, 100)
    # six_petal_flower(my_turtle, 100)
    # twelve_petal_flower(my_turtle, 100)
    # draw_triangle(my_turtle, 100)
    # draw_hexagon(my_turtle, 100)
    # color_spiral(my_turtle, 12, 50, wn)
    color_triangle_spiral(my_turtle, 12, 50, wn)
    wn.exitonclick()