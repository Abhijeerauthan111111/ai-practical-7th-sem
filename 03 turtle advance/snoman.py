import turtle
import time

screen = turtle.Screen()
screen.bgcolor("skyblue")
t = turtle.Turtle()
t.speed(0)
t.pensize(2)

# Function to draw circle
def draw_circle(color, radius, x, y):
    t.penup()
    t.fillcolor(color)
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Draw snow base (bottom circle)
draw_circle("white", 60, 0, -150)

# Draw middle circle
draw_circle("white", 40, 0, -30)

# Draw head (top circle)
draw_circle("white", 30, 0, 50)

# Draw eyes
draw_circle("black", 5, -15, 100)
draw_circle("black", 5, 15, 100)

# Draw carrot nose
t.penup()
t.goto(0, 85)
t.pendown()
t.fillcolor("orange")
t.begin_fill()
for i in range(3):
    t.forward(20)
    t.left(120)
t.end_fill()
 
# Draw arms
t.pensize(3)
t.penup()
t.goto(-50, 0)
t.pendown()
t.setheading(160)
t.color("brown")
t.forward(70)

t.penup()
t.goto(50, 0)
t.pendown()
t.setheading(20)
t.forward(70)

screen.mainloop()