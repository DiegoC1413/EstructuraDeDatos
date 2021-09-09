lista = [1,2,3,4,5]
def sumar (lista):
    if lista == []:
        suma = 0
    else:
        suma = lista[0] + sumar(lista[1:])
    return suma
print(sumar(lista))
