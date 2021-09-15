from turtle import Turtle

alignment = "center"
font = ("Arial", 24, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.points = 0
        self.penup()
        self.goto(0, 270)
        self.pendown()
        self.color("grey")
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.points}", align=alignment, font=font)

    def add_point(self):
        self.points += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.pendown()
        self.write("GAME OVER", align=alignment, font=font)
