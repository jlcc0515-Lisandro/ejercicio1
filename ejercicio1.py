nombre = input("nombre del estudiante: ")
suma_notas = 0

for i in range(1, 6):
    nota = float(input(f"ingresa la nota {i}: "))
    suma_notas += nota

promedio = suma_notas / 5
print(f"estudiante: {nombre}")
print(f"promedio final: {promedio:.2f}")