import random

x = random.randint(1,100)

print ("Tipp eit tal mellom 1 og 100!")

y = int( input())

teller = 0

while x != y:
    
    if y < x : print ("Høgare")

    if y > x : print ("Lavare")

    teller = teller + 1
    print ("Nytt forsøk!")
    

    y = int( input())


## for å kombinera må teller bli string
    
print ("Riktig på " + str(teller) + " forsøk")




