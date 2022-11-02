print("Numeros enteros pisitivos")
i = int(input('Ingrese un numero entero positivo: '))

suma = 0

while i >= 0:
    if i % 2 == 0:
        print(i)
        suma = suma+i
    i-=1

print("Numero ingresado es: ", i)
print("Sumatoria de numeros pares: ", suma)
