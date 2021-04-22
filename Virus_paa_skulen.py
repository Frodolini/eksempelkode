

import turtle as t
import random as r
import time

t.screensize()
t.setup(width = 1.0, height = 1.0)

for f in range(4):
    t.forward(100)
    t.left(90)
t.forward(25)
t.write("Stord vgs")


for x in range(300):
    t.hideturtle()
    t.penup()
    t.goto(r.randint(-580,580),r.randint(-280,280))
    t.pendown()
    t.dot(12,"Red")
    if t.xcor() > 0 and t.xcor() < 100 and t.ycor() > 0 and t.ycor() <100:
            t.goto(-20,280)
            t.bgcolor(("Yellow"))
            t.bgcolor("Orange")
            time.sleep(0.5)
            t.bgcolor("Black")
            time.sleep(0.5)
            t.bgcolor("Orange")
            time.sleep(0.5)
            t.bgcolor("Yellow")
            t.write("Det er virus på skulen",align='center', font=('Arial', 30, "normal"))
        
    
    





input("Trykk enter når klar")