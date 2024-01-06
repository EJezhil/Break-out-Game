from turtle import Turtle

class Score:
    def __init__(self):
        self.SCORES = 0

        with open('high_score.txt') as self.read_high_score:
            self.HIGH_SCORE = self.read_high_score.read()
            # print(self.HIGH_SCORE)

        self.show_score()
        self.show_high_score()

    def show_score(self):
        self.score = Turtle()
        self.score.penup()
        self.score.hideturtle()
        self.score.goto(-550, 360)
        self.score.color('green')
        self.score.write(f"SCORE: {self.SCORES}", font=('Arial', 18, 'bold'))
        return self.score

    def show_high_score(self):
        self.score1 = Turtle()
        self.score1.penup()
        self.score1.hideturtle()
        self.score1.goto(0, 360)
        self.score1.color("blue")
        self.score1.write(f"HIGH SCORE: {self.HIGH_SCORE}", align='center', font=('Arial', 18, 'bold'))
        return self.score1


    def reset_score(self):
        self.score.clear()
        self.SCORES+=10
        self.show_score()

    def increase_high_score(self):
        if self.SCORES > int(self.HIGH_SCORE):
            self.HIGH_SCORE = self.SCORES
            with open("high_score.txt",mode="w") as self.write_high_score:
                self.write_high_score.write(str(self.HIGH_SCORE))

        self.score.clear()
        self.SCORES = 0
        self.show_score()
        self.score1.clear()
        self.show_high_score()

