import turtle

# Create turtle object and screen
t = turtle.Turtle()
screen = turtle.Screen()

# Set up background color
screen.bgcolor("yellow")
t.speed(0)  # Fastest speed

# Draw face
t.penup()
t.goto(0, -100)
t.pendown()
t.fillcolor("yellow")
t.begin_fill()
t.circle(100)
t.end_fill()

# Draw eyes
# Left eye
t.penup()
t.goto(-40, 30)
t.pendown()
t.fillcolor("black")
t.begin_fill()
t.circle(15)
t.end_fill()

# Right eye
t.penup()
t.goto(40, 30)
t.pendown()
t.begin_fill()
t.circle(15)
t.end_fill()

# Draw nose
t.penup()
t.goto(0, 0)
t.pendown()
t.fillcolor("black")
t.begin_fill()
t.circle(5)
t.end_fill()

# Draw cheeks
# Left cheek
t.penup()
t.goto(-60, -20)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.circle(15)
t.end_fill()

# Right cheek
t.penup()
t.goto(60, -20)
t.pendown()
t.begin_fill()
t.circle(15)
t.end_fill()

# Draw mouth
t.penup()
t.goto(-30, -20)
t.pendown()
t.right(45)
t.circle(40, 90)

# Draw ears
# Left ear
t.penup()
t.goto(-70, 100)
t.pendown()
t.fillcolor("yellow")
t.begin_fill()
t.setheading(135)
t.forward(60)
t.right(90)
t.forward(60)
t.end_fill()

# Right ear
t.penup()
t.goto(70, 100)
t.pendown()
t.begin_fill()
t.setheading(45)
t.forward(60)
t.left(90)
t.forward(60)
t.end_fill()

# Draw body
t.penup()
t.goto(-50, -100)
t.pendown()
t.fillcolor("yellow")
t.begin_fill()
t.setheading(-90)
t.circle(50, 180)
t.setheading(0)
t.forward(100)
t.setheading(90)
t.circle(50, 180)
t.end_fill()

# Draw arms
# Left arm
t.penup()
t.goto(-50, -100)
t.pendown()
t.setheading(-135)
t.forward(50)
t.backward(50)

# Right arm
t.penup()
t.goto(50, -100)
t.pendown()
t.setheading(-45)
t.forward(50)
t.backward(50)

# Draw legs
# Left leg
t.penup()
t.goto(-30, -200)
t.pendown()
t.setheading(-90)
t.forward(50)
t.backward(50)

# Right leg
t.penup()
t.goto(30, -200)
t.pendown()
t.setheading(-90)
t.forward(50)
t.backward(50)

# Hide turtle and display
t.hideturtle()
screen.exitonclick()
