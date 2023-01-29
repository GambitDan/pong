from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        """paddle initialisation"""
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        """move paddle up"""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """move paddle down"""
        new_y = self.ycor() -  20
        self.goto(self.xcor(), new_y)