print("Registro de nota")
nombre = input("Ingrese nombre del estudiante: ")
nota = float(input("Ingrese nota final: "))
print("Estudiante:", nombre)
print("Nota final:", nota)

if nota>4.0:
    print(f"El estudiante aprobo con un {nota}")
else:
    print(f"El estudiante desaprobo con un {nota}")