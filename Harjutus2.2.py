#Jarek Mandre (15.10.2025)
#Harjutus 2.1

import turtle

aken = turtle.Screen()
aken.setup(width=500, height=500)
aken.title("Sinilill, Jarek")
t = turtle.Turtle()
t.speed("fastest")
t.pensize(10)

t.penup()
t.goto(0,100)
t.pendown()
t.pencolor("green")
t.right(90)
t.fd(200)
t.penup()
t.right(90)
t.goto(0,50)
t.fd(10)
for i in range(3):
    turtle.fd(200)
    turtle.lt(120)

turtle.done()