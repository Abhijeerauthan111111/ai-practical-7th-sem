import turtle
import time

# Set up the screen
screen = turtle.Screen()
screen.title("Indian National Flag")
screen.bgcolor("white")

# Create turtle object
t = turtle.Turtle()
t.speed(0)
t.pensize(2)

# Function to draw rectangle
def draw_rectangle(color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(300)
        t.right(90)
        t.forward(60)
        t.right(90)
    t.end_fill()

# Function to draw Ashoka Chakra
def draw_chakra():
    t.pencolor("#000080")
    t.pensize(1)
    radius = 30
    t.right(90)
    t.forward(30)
    t.left(90)
    
    # Draw 24 spokes
    for _ in range(24):
        t.forward(radius)
        t.backward(radius)
        t.left(15)

# Draw the flag
t.penup()
t.goto(-150, 150)
t.pendown()

# Draw saffron rectangle
draw_rectangle("#FF9933")

# Draw white rectangle
t.penup()
t.right(90)
t.forward(60)
t.left(90)
t.pendown()
draw_rectangle("white")

# Draw green rectangle
t.penup()
t.right(90)
t.forward(60)
t.left(90)
t.pendown()
draw_rectangle("#138808")

# Draw Ashoka Chakra
t.penup()
t.goto(0, 90)
t.pendown()
draw_chakra()

# Hide turtle and display
t.hideturtle()
screen.mainloop()