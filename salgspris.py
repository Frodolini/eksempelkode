## Program til å rekna ut pris på varer til salgs.

## Først hente eg inn orginalpris

orginalPris = float(input("Kva er prisen på vara før salsperioden? "))

## Så vil eg henta inn kor mykje me skal gje i avslag i prosent

avslagProsent =int(input("Kor mange % er avslaget på? "))

## Så må eg rekna ut kva ny pris blir

nyPris =orginalPris - (orginalPris / 100 * avslagProsent)

print (("Den nye prisen blir: "),(%.3f) % nyPris)
