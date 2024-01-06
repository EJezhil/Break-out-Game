import time
from turtle import Turtle

class Health:
    def __init__(self):
        self.HEALTH = 5
        self.show_health()

    def show_health(self):
        self.health_t = Turtle()
        self.health_t.penup()
        self.health_t.goto(430, 360)
        self.health_t.color('deep pink')
        self.health_t.hideturtle()
        self.health_t.write(f"HEALTH: {self.HEALTH}", font=('Arial', 18, 'bold'))


    def reset_health(self):
        time.sleep(1)
        self.health_t.clear()
        self.HEALTH-=1
        self.show_health()
