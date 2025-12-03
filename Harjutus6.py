#Ülesanne 6
#Jarek Mandre, 03.12
import math
import turtle

turtle.speed(0)
mootkava = 50

nurk = math.radians(53)
korgus = 4.4

kaugus = round(korgus / math.tan(nurk),2)
pikkus = round(math.sqrt(math.pow(korgus,2) + math.pow(kaugus,2)),2)

print(pikkus)
print(kaugus)
print(nurk)

turtle.fd(kaugus * mootkava)
turtle.lt(90)
turtle.fd(korgus * mootkava)
turtle.lt(143)
turtle.fd(pikkus * mootkava)

turtle.done