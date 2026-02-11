import turtle

t = turtle
screen = turtle.Screen()

t.speed(0)
pikkus = screen.numinput("Pikkuse sisestamine", "Kui pikk peab olema?", default=20, minval=0, maxval=200)
pikk = 10
t.penup()
t.goto(-450, 0)
t.pendown()
number = 0
for i in range(1, int(pikkus)):
    t.lt(90)
    t.fd(20+pikk)
    t.bk(20+pikk)
    t.rt(90)
    t.fd(20)
    if i%5==0:
        pikk = 10
    else:
        pikk = 0

t.penup()
t.goto(-450, 0)
t.lt(90)
t.fd(20+pikk+10)
t.rt(90)
for i in range(0,int(pikkus)):
    if i%5==0:
        t.write(number, font=("Arial", 8, "normal"))
    t.fd(20)
    number += 1

t.done()