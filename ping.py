import subprocess as s
print ("IP?")
ip = input()
if(s.call(["ping",ip])==0):
    print ("Din IP er i live :)")
else:
    print ("Sjekk din IP")
