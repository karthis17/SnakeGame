from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.goto(0, 275)
        self.write(f"Score : {self.score}", align="center", font=("Poppins", 14, "bold"))

    def increaseScore(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}", align="center", font=("Poppins", 14, "bold"))

    def gameOver(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Poppins", 14, "bold"))
