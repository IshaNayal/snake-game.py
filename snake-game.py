import turtle
import time
import random
screen = turtle.Screen()
screen.title("🐍 Snake Game")
screen.bgcolor("dark blue") 
screen.setup(width=600, height=600)
screen.tracer(0)


border = turtle.Turtle()
border.penup()
border.goto(-290, 290)
border.pendown()
border.pensize(4)
border.color("white")
for _ in range(4):
    border.forward(580)
    border.right(90)
border.hideturtle()


head = turtle.Turtle()
head.speed(0)
head.shape("square")  
head.color("darkgreen")
head.penup()
head.goto(0, 0)
head.direction = "stop"


food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("orange")
food.penup()
food.goto(0, 100)


segments = []   


score = 0
high_score = 0
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Arial", 24, "bold"))


def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)


screen.listen()
screen.onkeypress(go_up, "u")
screen.onkeypress(go_down, "d")
screen.onkeypress(go_left, "l")
screen.onkeypress(go_right, "r")


while True:
    screen.update()

   
    if abs(head.xcor()) > 280 or abs(head.ycor()) > 280:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Arial", 24, "bold"))

    if head.distance(food) < 20:
        food.goto(random.randint(-270, 270), random.randint(-270, 270))
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("darkgreen")
        new_segment.penup()
        segments.append(new_segment)
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Arial", 24, "bold"))

  
    for i in range(len(segments) - 1, 0, -1):
        segments[i].goto(segments[i - 1].xcor(), segments[i - 1].ycor())
    if segments:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    for segment in segments:
        if head.distance(segment) < 10:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for seg in segments:
                seg.goto(1000, 1000)
            segments.clear()
            score = 0
            pen.clear()
            pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Arial", 24, "bold"))

    time.sleep(0.2)
