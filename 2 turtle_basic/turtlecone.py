import turtle

t = turtle.Turtle()

screen = turtle.Screen()
t.speed(0)  # Fastest speed

t.left(120)     # Turn 120 degrees
t.forward(100)  # Second side
t.left(120)     # Turn 120 degrees
t.forward(100)  # Third side
# t.left(120)
# Drawing an oval
t.penup()
t.goto(-100,-10)
t.pendown()
t.left(80)
 
for _ in range(2):  # Create oval with 2 semicircles
    t.circle(70,90)  # Draw a quarter circle
    t.circle(7,90)  # Reduced radius from 20 to 10 for smaller width



screen.exitonclick();