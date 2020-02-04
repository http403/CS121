from time import sleep
from turtle import Turtle, done

from shapes import (
    rectangle,
    trapezoid,
    window
)

if __name__ == '__main__':
    # Set up the turtle
    turtle = Turtle()

    # set turtle properties
    turtle.screen.mode("logo")
    turtle.screen.screensize(canvwidth=960, canvheight=810)
    # turtle.screen.bgcolor("#80d9ff")

    turtle.penup()  # make sure it don't draw anything

    # get how big the canvas be
    canvas_height = turtle.screen.window_height()
    canvas_width = turtle.screen.window_width()

    # Start drawing the house

    # draw wall
    # make it 1/3 below the center
    turtle.home()
    turtle.sety(-130)
    rectangle(
        t=turtle,
        length=700,
        height=400,
        color=None
    )

    # draw roof
    turtle.home()
    turtle.sety(70)
    trapezoid(
        t=turtle,
        top=750,
        base=800,
        height=175,
        color=None
    )

    # draw window 1
    turtle.home()
    turtle.setpos(-195, -60)
    window(t=turtle, width=125, height=None)
    # draw window 2
    turtle.home()
    turtle.setpos(195, -60)
    window(t=turtle, width=125, height=None)

    # draw door
    turtle.home()
    turtle.sety(-192.5)
    rectangle(
        t=turtle,
        length=150,
        height=275,
        color=None
    )

    # draw door knob
    turtle.home()
    turtle.setpos(-55, -192.5)
    turtle.pd()
    turtle.circle(radius=5)
    turtle.pu()

    # draw chimney
    turtle.home()
    turtle.setpos(-175, 295)
    rectangle(
        t=turtle,
        length=50,
        height=100,
        color=None
    )

    # hide the turtle for better visual
    sleep(0.5)
    turtle.hideturtle()

    # Ensure windows stays open after done drawing
    done()
