ruta=" "*50
print(ruta,"+","-"*16,"+")
print(ruta,"|  Te21C           |")
print(ruta,"|  Anton Ahlm      |")
print(ruta,"+","-"*16,"+\n\n")

import math 
import sys

print("Skriv p och q varden (Heltal)")
p=int(input("P = "))
q=int(input("Q = "))

    

del1= -p/2
del2=(p/2)**2
if del2-q <0:
    print("+----------------------------+")
    print("| Talet har inga losningar   |")
    print("|                            |")
    print("+----------------------------+")
    
else: 
    del3=math.sqrt(del2-q) 
    pq1=del1+del3 
    pq2=del1-del3 

    if pq1==0 and pq2!=0: 
        print("x1=0 \nx2=",pq2)
    if pq2==0 and pq1!=0: 
        print("x1=",pq1," \nx2=0")
    if pq1!=0 and pq2!=0: 
        print("x1=",pq1,"\nx2=",pq2)
    if pq1==0 and pq2==0:
        print("Talet har inga losningar")






