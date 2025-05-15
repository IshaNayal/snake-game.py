import turtle
import time
import random

# Set up the screen
screen = turtle.Screen()
screen.title("🐍 Snake Game")
screen.bgcolor("pink")  # Background improved
screen.setup(width=600, height=600)
screen.tracer(0)# disables automatic screen updates, which improves performance by manually controlling when the screen updates.

# Draw border
border = turtle.Turtle()
border.penup()
border.goto(-290, 290)
border.pendown()
border.pensize(4)
border.color("black")
for _ in range(4):
    border.forward(580)
    border.right(90)
border.hideturtle()

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")  # Changed from square to circle
head.color("darkgreen")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("orange")
food.penup()
food.goto(0, 100)

# Snake body segments
segments = []   # An empty list to store the snake's growing body parts.

# Score setup
score = 0
high_score = 0
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Arial", 24, "bold"))

# Movement functions
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

# Controls
screen.listen()
screen.onkeypress(go_up, "u")
screen.onkeypress(go_down, "d")
screen.onkeypress(go_left, "l")
screen.onkeypress(go_right, "r")

# Game loop
while True:
    screen.update()

    # Border collision
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

    # Food collision
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

    # Body movement
    for i in range(len(segments) - 1, 0, -1):
        segments[i].goto(segments[i - 1].xcor(), segments[i - 1].ycor())
    if segments:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    # Self-collision
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
