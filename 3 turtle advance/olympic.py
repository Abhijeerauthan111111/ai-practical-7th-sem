import turtle

screen = turtle.Screen()
screen.title("Olympic Symbol")

t = turtle.Turtle()
t.width(6)
t.speed(0)

# Function to draw a circle with specific color
def draw_circle(color):
    t.pendown()
    t.color(color)
    t.circle(50)
    t.penup()

# Starting position
t.penup()
t.goto(-120, 0)

# Draw blue circle
draw_circle("blue")

# Draw yellow circle
t.goto(-60, -50)
draw_circle("yellow")

# Draw black circle
t.goto(0, 0)
draw_circle("black")

# Draw green circle
t.goto(60, -50)
draw_circle("green")

# Draw red circle
t.goto(120, 0)
draw_circle("red")

screen.mainloop()