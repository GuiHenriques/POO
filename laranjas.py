import turtle
from time import sleep

t = turtle.Turtle()
x = 10
# color
t.fillcolor('orange')
t.up()
t.bk(400)
t.down()

for i in range(10):
    t.begin_fill()
    t.circle(x*i)
    t.up()
    t.fd(x*i + x*(i+1))
    t.down()
    t.end_fill()

sleep(3)