# Laga ein kortstokk og trekka fem tilfeldige kort
import random as r

farge = ["Hjerter", "Ruter", "Kløver", "Spar"]
tal = ["Ess",2,3,4,5,6,7,8,9,10,"Knekt","Dame","Konge"]
kortstokk = []
antall_kort = 0
mittkort = ""
for f in farge:
    for t in tal:
        print(f,t, end= "--")
        antall_kort +=1
        mittkort= f, t
        kortstokk.append(mittkort)

print()
print("Ferdig!, det er no ", antall_kort, "kort i stokken")
print()
print("Dine kort er:")
print(*kortstokk[r.randrange(0, 52)],end=" //// ")
print(*kortstokk[r.randrange(0, 52)],end=" //// ")
print(*kortstokk[r.randrange(0, 52)],end=" //// ")
print(*kortstokk[r.randrange(0, 52)],end=" //// ")
print(*kortstokk[r.randrange(0, 52)],end=" //// ")
