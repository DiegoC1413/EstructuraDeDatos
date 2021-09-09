print (" SERIE FIBONACCI ")

def fibo(numero):
    if numero < 2:
        return numero
    else:
        return (fibo(numero-1)+fibo(numero-2))

numero = int(input("Digite su numero: "))
print(fibo(numero))






