# Laga eit rutenett med løkker (og kanskje funksjon).

import turtle as t
t.hideturtle()
t.speed(10)
y=0
t.fillcolor("yellow")
t.begin_fill()
for r in range(2):
    for k in range(2):
        for l in range (4):
            t.forward(50)
            t.left(90)
        t.up()
        t.forward(50)
        t.down()

    t.up()
    y=y+50
    t.goto(0,y)
    t.down()
    #t.write(t.pos())
t.end_fill()
input()
