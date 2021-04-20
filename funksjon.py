import turtle as t
import time

def firkant():
    for n in range (4):
        t.forward(100)
        t.left(90)
    t.up()
    t.goto(0,-50)
    t.write("Her var firkanten din")
    
def sirkel():
    t.circle(50)
    t.up()
    t.goto(-50,-50)
    t.write("Her var sirkelen din")
    

v = input("Vil du ha firkant (F) eller sirkel(S)? ")

if v == "F":
    firkant()
else:
    sirkel()

time.sleep(5)
