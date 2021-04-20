

with open("logg1.txt", "r") as f:
    file_str = str(f.read())
    f.close()
last_chr = file_str[-2]
print(last_chr)
