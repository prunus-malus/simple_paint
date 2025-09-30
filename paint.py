from turtle import *

t = Turtle()
t.color('blue')
t.width(5)
t.speed(0)
t.shape('circle')

def draw(x, y):
    t.goto(x, y)

t.ondrag(draw)

def move(x, y):
    t.up()
    t.goto(x, y)
    t.down()

scr = t.getscreen()
scr.listen()
scr.onscreenclick(move)
def Green():
    t.color('green')
def Blue():
    t.color('blue')
def Red():
    t.color('red')
scr.onkey(Green, 'g')
scr.onkey(Blue, 'b')
scr.onkey(Red, 'r')
def key_right():
    t.goto(t.xcor() + 5, t.ycor())
def key_left():
    t.goto(t.xcor() - 5, t.ycor())
def key_up():
    t.goto(t.xcor(), t.ycor() + 5)
def key_down():
    t.goto(t.xcor(), t.ycor() - 5)
scr.onkey(key_down, 'Down')
scr.onkey(key_left, 'Left')
scr.onkey(key_right, 'Right')
scr.onkey(key_up, 'Up')
scr.onkey(t.begin_fill, 'z')
scr.onkey(t.end_fill, 'x')
