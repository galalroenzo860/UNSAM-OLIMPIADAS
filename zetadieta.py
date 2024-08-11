import math

def zetadieta(C,P,G):
    Cfin= (math.ceil(C/27))*105
    Pfin= (math.ceil(P/30))*120
    Gfin= (math.ceil(G/1))*9
    caloriaTotales = Cfin+Pfin+Gfin
    print(f"Las calorias totales a consumir son de: {caloriaTotales}")
    
print("Ingrese el valor de C")
cIng = int(input())
print("Ingrese el valor de P")
pIng = int(input())
print("Ingrese el valor de G")
gIng = int(input())

zetadieta(cIng,pIng,gIng)