print("Por Favor ingrese numeros enteros posotivos: .")
a= int(input('Ingrese el primer Numero: '))
b = int(input('Ingrese el segundo numero: '))
c = int(input('Ingrese el tercer numero: '))
d = int(input('Ingrese el cuarto Numero: '))

lista = [a, b, c, d ]
def orden(e):
    e.sort() # Para ordenar numeros de forma descendente y si son letras, alfabeticamente
    e.reverse()# Para capturar el srot() ordenado, y reversed lo invierte
    for h in e:
        print(h)

orden(lista) # llama la funcion y muestra en pantalla
