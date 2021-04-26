# Laga eit rutenett med løkker (og kanskje funksjon).

import turtle as t
y=0
for r in range(5):
    for k in range(3):
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

