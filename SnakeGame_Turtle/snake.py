from turtle import Turtle

"""The snake starts with a length of 3 blocks and their positions are initialised """
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

"""global constants -> signify direction and distance moved by the snake  """
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """Defining head of snake, creating the snake, adding segments in the snake"""

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """ Creating the 3 block snake """
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Defining the shape, color, position of the snake """
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """appending extra length at the end of the snake """
        self.add_segment(self.segments[-1].position())

    def move(self):
        """ Defining the movement of the snake -> The HARDEST part of the project. Here the next snake blocks follow
        the previous snake blocks. Otherwise, the blocks will move independently """
        """ This can also be understood by linked list type approach """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            # Assigning the incoming snake tail to follow the previous block
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    """ The following four functions define -> The snake cannot go back in the opposite direction instantly """

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
