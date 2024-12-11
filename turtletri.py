import turtle

# Create a turtle object
t = turtle.Turtle()

# Set up the screen
screen = turtle.Screen()
t.speed(0)  # Fastest speed

# Draw a triangle
t.forward(100)  # First side
t.left(120)     # Turn 120 degrees
t.forward(100)  # Second side
t.left(120)     # Turn 120 degrees
t.forward(100)  # Third side

# Keep the window open until clicked
screen.exitonclick()
