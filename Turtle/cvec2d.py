from turtle import Vec2D


class CVec2D(Vec2D):
    def xcor(self):
        return self[0]

    def ycor(self):
        return self[1]