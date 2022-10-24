print("Ejercicios de Horas, diferenciad: ")
print("Ingrese dos horas distintas, procure que el primero que la hora sea mayor que la segunda:")
a = int(input('Ingrese la primera hora de 0 a 24 hrs:  '))
b = int(input('Ingrese los minutos de 0 a 60:  '))
c = int(input('Ingrese los segundos de 0 a 60:  '))

print("Ingrese los segundos datos:")
d = int(input('Ingrese la segunda hora de 0 a 24 horas:   '))
e = int(input('Ingrese los minutos de 0  60:  '))
f = int(input('Ingrese los segundos de 0 a 60 :  '))

total1 = a - d #Restar las horas
total2 = total1 * 60 *60 #horas restadas y multiplicado para convertir en segundos
total3 = b - e # Minutos restados
total4 = total3 * 60 # Se multiplico los minutos en segundos
if total4 < 0:
    total4 *= -1
total5 = c - f # Se restaron los segundos
if total5 < 0:
    total5 *= -1
restar_total = total2 - total4
suma_total = restar_total + total5


print("EL total de la resta de hora es: ", total1)
print("El Total convertido de hora a segundos es: ", total2)
print("Total convertido de minutos a  segundos es: ", total4)
print("TOtal de segundos restados es: ", total5)

print(" DIFERENCIA DE SEGUNdOS ES: ", suma_total)


