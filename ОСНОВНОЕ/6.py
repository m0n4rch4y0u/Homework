from turtle import *
print(19 * 11 + 8 * 5)
lt(90)
tracer(0)
m = 25
for _ in range(2):
    fd(10 * m)
    rt(90)
    fd(18 * m)
    rt(90)
up()
fd(5 * m)
rt(90)
fd(7 * m)
lt(90)
down()
for _ in range(2):
    fd(10 * m)
    rt(90)
    fd(7 * m)
    rt(90)

up()
for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x * m, y * m)
        dot('blue')
done()
