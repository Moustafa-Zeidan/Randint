import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Turtle Screensaver")
screen.setup(width=800, height=600)
screen.tracer(0)

# Create a turtle
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.width(2)

colors = ["red", "orange", "yellow", "green", "blue", "purple", "cyan", "white"]

def random_walk():
    t.penup()
    t.goto(random.randint(-390, 390), random.randint(-290, 290))
    t.pendown()
    t.pencolor(random.choice(colors))
    angle = random.randint(0, 360)
    t.setheading(angle)
    length = random.randint(50, 200)
    t.forward(length)

def draw_screensaver():
    for _ in range(50):
        random_walk()
        screen.update()
    screen.ontimer(draw_screensaver, 1000)

draw_screensaver()
screen.mainloop()