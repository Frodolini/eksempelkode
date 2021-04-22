import random

for x in range (10):

 x=0

 while x!=7 :
    thislist = [random.randint(1,34), random.randint(1,34), random.randint(1,34), random.randint(1,34), random.randint(1,34), random.randint(1,34), random.randint(1,34)]
    thislist.sort()
    thislist = list(dict.fromkeys(thislist))
    

    x = (len(thislist))


 print (thislist)



