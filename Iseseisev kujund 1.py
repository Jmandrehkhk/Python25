#Jarek Mandre (03.01.2026)
#Iseseisev kujund 1

import turtle

t = turtle.Turtle()
t.speed(5)  
t.pensize(2)
t.hideturtle()
kulje_pikkus = 100

for a in range(6):
    t.forward(kulje_pikkus)  
    t.left(120)             
    t.forward(kulje_pikkus)  
    t.left(120)             
    t.forward(kulje_pikkus)  
    t.left(180) 

turtle.done()