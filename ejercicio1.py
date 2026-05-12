continuar = "si"

while continuar == "si":
    print("sistema de evaluación academica")
    nombre = input("nombre del estudiante: ")
    
    suma_notas = 0 
    
    for i in range(1, 6):
        nota = float(input(f"ingresa la nota {i}: "))
        suma_notas += nota
        
    promedio = suma_notas / 5
    print(f"estudiante: {nombre}")
    print(f"promedio final: {promedio:.2f}")
    
    if promedio >= 4.5:
        print("estado: Excelente")
    elif promedio >= 3.0:
        print("estado: aprobado")
    else:
        print("estado: reprobado")
        
    continuar = input("¿Deseas evaluar a otro estudiante? (si/no): ")

print("gracias por usar el sistema ¡muchos exitos en tu evaluacion!")