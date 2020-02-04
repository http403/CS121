from cvec2d import CVec2D

from turtle import RawTurtle
from typing import Optional, Tuple, Union


# Define some types for type hinting
Color = Union[Tuple[str, str], Tuple[int, int, int]]


def _color_clean(t: RawTurtle):
    t.color((0, 0, 0))


def rectangle(t: RawTurtle, length: float, height: Optional[float], color: Optional[Color]) -> None:
    # if width not set, we are drawing a square
    if not height:
        height = length

    # if color specified
    if color:
        if type(color[0]) == str:
            t.color(*color)
        else:
            t.color(color)
        t.begin_fill()

    # we're now at the top-right
    t.setposition(t.position()[0] + length / 2, t.position()[1] + height / 2)
    t.pd()

    # actual shape
    t.sety(t.ycor() - height)
    t.setx(t.xcor() - length)
    t.sety(t.ycor() + height)
    t.setx(t.xcor() + length)

    # finishing things up
    t.pu()
    if color:
        t.end_fill()
        _color_clean(t)


def trapezoid(t: RawTurtle, top: float, base: float, height: float, color: Optional[Color]) -> None:
    # if color specified
    if color:
        if type(color[0]) == str:
            t.color(*color)
        else:
            t.color(color)
        t.begin_fill()

    # draw from the bottom-mid
    t.pd()

    # save the starting point
    ref_pos = CVec2D(t.xcor(), t.ycor())

    # actual shape
    t.setx(t.xcor() + base/2)
    t.setpos(ref_pos.xcor() + top/2, ref_pos.ycor() + height)
    t.setx(t.xcor() - top)
    t.setpos(ref_pos.xcor() - base/2, ref_pos.ycor())
    t.setx(ref_pos.xcor())

    # finishing up
    t.pu()
    if color:
        t.end_fill()
        _color_clean(t)


def window(t: RawTurtle, width: float, height: Optional[float]):
    # if height not set
    if not height:
        height = width

    # save the starting point
    ref_pos = CVec2D(t.xcor(), t.ycor())

    corners = [
        CVec2D(ref_pos.xcor() + width / 4, ref_pos.ycor() + height / 4),
        CVec2D(ref_pos.xcor() - width / 4, ref_pos.ycor() + height / 4),
        CVec2D(ref_pos.xcor() + width / 4, ref_pos.ycor() - height / 4),
        CVec2D(ref_pos.xcor() - width / 4, ref_pos.ycor() - height / 4)
    ]

    for corner in corners:
        t.setpos(corner.xcor(), corner.ycor())
        rectangle(
            t=t,
            length=width/2,
            height=height/2,
            color=("black", "white")
        )
