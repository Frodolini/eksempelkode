# Døme funksjon med retur

#Lager funksjon og ber den returnera arealet
def areal(x,y):
    arealet = x * y
    return arealet

x=areal(200,300) # sender 200 og 300 over i funksjonen og får tilbake arealet
print("arealet er:",x) #Skriv ut arealet
