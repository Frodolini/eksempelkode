# Program som spør etter eit ord og skriv ut sha-256 hash.

import hashlib

# Hentar inn noko frå brukaren
n = input("Kva vil du hasha? ")

# Gjer string om til datatypen bytes.
nb = bytes(n, encoding='utf-8')

# Reknar ut hash.
a= hashlib.sha256(nb).hexdigest()

# Skriv ut resultatet
print("Sha256 av det du ville hasha er", a)





