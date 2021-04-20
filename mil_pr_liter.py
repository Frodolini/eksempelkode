## Her skal eg spør etter kjøyrelengde og tid brukt og rekna ut forbruk pr mil.

lengde_kjørt = int(input("kor mange mil har du kjørt "))

liter_brukt = int(input("Kor mange liter har du brukt? "))

mil_pr_liter = lengde_kjørt / liter_brukt

print("Bilen din kjører", format(mil_pr_liter, ".1f"), "mil pr liter")

