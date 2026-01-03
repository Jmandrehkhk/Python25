#Jarek Mandre
#10.11.25

import turtle
t = turtle.Turtle()
aken = turtle.Screen()
aken.setup(width=500, height=500)
aken.title("Sinilill - Jarek")


#vars
t.penup()
t.goto(0,-200)
t.pendown()
t.pensize(10)
t.pencolor("green")
t.lt(90)
t.fd(200)
#õis
t.begin_fill()
t.pensize(10)
t.color("blue")
t.rt(90)
t.circle(60)
t.end_fill()

#emakas
t.penup()
t.goto(0,50)
t.pendown()
t.pencolor("yellow")
t.pensize(20)
t.circle(10)

t.penup()
t.goto(-20,-100)
t.pendown()
t.pensize(10)
t.begin_fill()
t.color("green", "green")
t.lt(90)
t.fd(40)
t.lt(135)
t.fd(35)
t.lt(100)
t.fd(30)
t.end_fill()

turtle.done()
