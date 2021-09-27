import math

print("ECUACION CUADRATICA ''2X^2+Bx+C''")

a = int(input("DAME EL VALOR DE A: "))
b = int(input("DAME EL VALOR DE B: "))
c = int(input("DAME EL VALOR DE C: "))

def chicarronera ():
    e = 0
    e = (b * b) - 4 * a* c
    if e < 0:
        print("NO EXISTE VALOR EN LOS REALES ")
    else:
        x1 = (-b + math.sqrt(e))/2*a
        x2 = (-b - math.sqrt(e))/2*a
        print(x1, x2)
(chicarronera())