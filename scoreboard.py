from turtle import Turtle

FONT = ('Arial', 16, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt") as data:
            self.high_score = int(data.read())

        self.color("white")
        self.penup()
        self.goto(x=0, y=265)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"score: {self.score} High Score: {self.high_score}", move=False, align="center", font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="W") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", move=False, align="center", font=('Arial', 24, 'normal') )

    def score_inc(self):
        self.score += 1
        self.update_score()

