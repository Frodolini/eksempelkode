# Døme på lister med klassen
import random as r

klassen = ["Elev1", "Elev2", "Elev3","Elev4", "Elev5", "Elev6", "Elev7", "Elev8", "Elev9"]

print(*klassen)

print("Antall elevar er:", len(klassen))

print("Dagens elev er", klassen[r.randrange(0,len(klassen))])
print("Dagens banditt er", klassen[r.randrange(0,len(klassen))])