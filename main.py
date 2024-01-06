import time
from turtle import *
from score import Score
from health import Health

addx = -10
addy = -10
health = 5
blocks = []
x = -550
y = 300
ball_spped = 0.04

window = Screen()
window.title("Breakout Game")
window.setup(1230, 800)
window.listen()
window.tracer(0)

start = True
# print(window.window_width(), window_height())

paddle = Turtle(shape="square")
paddle.color("lightblue")
paddle.penup()
paddle.shapesize(stretch_wid=1, stretch_len=6)
paddle.goto(0, -350)

ball = Turtle(shape="circle")
ball.color("red")
ball.penup()


for i in range(85):
    block = Turtle(shape="square")
    block.penup()
    block.color("lightgreen")
    block.shapesize(stretch_len=3, stretch_wid=2)
    blocks.append(block)
    # block.goto(550,350)
# print(blocks)

for i in blocks:
    i.goto(x, y)
    x += 70
    # print(f" x:{i.xcor()},y:{i.ycor()}")
    if i.xcor() > 500:
        x = -550
        y += -50


def paddle_left():
    paddle_x = paddle.xcor()
    paddle_y = paddle.ycor()
    paddle.goto(paddle_x - 40, paddle_y)


def paddle_right():
    paddle_x = paddle.xcor()
    paddle_y = paddle.ycor()
    paddle.goto(paddle_x + 40, paddle_y)


window.onkeypress(fun=paddle_left, key="Left")
window.onkeypress(fun=paddle_right, key="Right")


def move_ball():
    global addx
    global addy
    time.sleep(ball_spped)
    ballx = ball.xcor()
    bally = ball.ycor()
    ball.goto(ballx + addx, bally + addy)
    # print(ballx, bally)


# 1200 = -600, 600
# 800 = -400, 400
score = Score()
health = Health()

while start:
    move_ball()
    # print(f"paddle {paddle.xcor(), paddle.ycor()}")
    if paddle.xcor() > 550:
        paddle.goto(550, paddle.ycor())
    if paddle.xcor() < -550:
        paddle.goto(-550, paddle.ycor())

    if ball.xcor() < -380 and ball.ycor() < -380:
        addy *= -1
    elif ball.xcor() < -600:
        addx *= -1
    elif ball.xcor() > 580:
        addx *= -1
    elif ball.ycor() < -370:
        addy *= -1
        health.reset_health()
    elif ball.ycor() > 380:
        addy *= -1

    if ball.distance(paddle) < 50 and ball.ycor() < -310:
        addy *= -1
    # print(f"distance{ball.distance(paddle)}")
    if health.HEALTH == 0:
        print("Game Over")
        score.increase_high_score()
        exit()

    for i in blocks:
        if ball.distance(i) < 40:
            score.reset_score()
            i.reset()
            i.hideturtle()
            addy *= -1
            if ball_spped > 0.01:
                ball_spped = ball_spped - 0.01
            else:
                ball_spped = 0.01
    # print(score.SCORES)
    # print(ball_spped)
    window.update()

window.exitonclick()
