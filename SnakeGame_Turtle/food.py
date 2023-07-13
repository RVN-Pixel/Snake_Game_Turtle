from turtle import Turtle
import random


class Food(Turtle):
    """Setting the food/pill in the game which the snake eats. Super class is used here(inheritance) """
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        # shapesize multiplies by a certain factor
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """This function randomises the position of the blue circle within the coordinates given"""
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)
