# Skriv noko til ei tekstfil
f = open("filami1.txt", "a")
f.write(input("Kva tekst vil du ha i filadi?"))
f.close()
input("No har eg oppretta fila med teksten. Trykk enter om du vil lesa fila!")
f = open ("filami1.txt", "r")
print(f.read())
f.close()

import os

os.remove("filami1.txt")
