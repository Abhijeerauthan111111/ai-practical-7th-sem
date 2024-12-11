import turtle

t = turtle.Turtle()

screen = turtle.Screen()
t.speed(0) 

t.left(120)    
t.forward(100)  
t.left(120)     
t.forward(100) 
# t.left(120)
# Drawing an oval
t.penup()
t.goto(-100,-10)
t.pendown()
t.left(80)
 
for _ in range(2): 
    t.circle(70,90)  
    t.circle(7,90)  

screen.exitonclick();