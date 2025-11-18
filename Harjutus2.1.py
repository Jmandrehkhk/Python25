#Jarek Mandre (15.10.2025)
#Harjutus 2.1

import turtle

aken = turtle.Screen()
aken.setup(width=500, height=400)
aken.title("Olümpiarõngad, Jarek")
t = turtle.Turtle()
t.speed(0)
t.pensize(6)

t.penup()
t.goto(0,0)
t.pendown()
t.pencolor("black")
t.circle(50)

t.penup()
t.goto(-110,0)
t.pendown()
t.pencolor("blue")
t.circle(50)

t.penup()
t.goto(110,0)
t.pendown()
t.pencolor("red")
t.circle(50)

t.penup()
t.goto(55,-50)
t.pendown()
t.pencolor("green")
t.circle(50)

t.penup()
t.goto(-55,-50)
t.pendown()
t.pencolor("yellow")
t.circle(50)



turtle.done()
