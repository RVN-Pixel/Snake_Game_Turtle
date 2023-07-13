from turtle import Turtle

# The alignment and font attributes are kept global -> For the programmer of the game to change the appearance at any
# time
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """Inheritance(super class) is used to keep a check on score of the person"""
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """The updated score is displayed using this function"""
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """When the game finishes -> GAME OVER will be displayed in the middle """
        self.goto(0, 0)
        # write method helps to align the text
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """For updating the score whenever the player scores a point. Passing the function update_scorecard to
        display the updated result"""
        self.score += 1
        self.clear()
        self.update_scoreboard()
