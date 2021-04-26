# Døme laga eit rutenett med løkker og funksjonar.

import turtle as t

def ei_rute():
    t.forward(50)
    t.left(90)

def rutenett():
    t.hideturtle()
    t.speed(10)
    y=0
    t.fillcolor("yellow")
    t.begin_fill()
    for r in range(4):
        for k in range(3):
            for l in range (4):
                ei_rute()
            t.up()
            t.forward(50)
            t.down()
        t.up()
        y=y+50
        t.goto(0,y)
        t.down()
    t.end_fill()

rutenett()
input()
