print("Hola Estudiate, encotraremos tu promedio!")
numero_de_estudiantes  = int(input("Para cuantas personas necesitas este promedio? "))
estudiantes = []

for n in range(numero_de_estudiantes):
    nombre_del_estudiante = input(f"Ingrese el nombre del estudiante {n+1}: ")
    matricula = input(f"Ingrese la matricula del estudiante {n+1}: ")
    nota_1 = float(input(f"Ingrese la nota 1 del estudiante {n+1}: "))
    nota_2 = float(input(f"Ingrese la nota 2 del estudiante {n+1}: "))
    nota_3 = float(input(f"Ingrese la nota 3 del estudiante {n+1}: "))
    nota_4 = float(input(f"Ingrese la nota 4 del estudiante {n+1}: "))

    if nota_1 < 0 or nota_2 < 0 or nota_3 < 0 or nota_4 < 0: 
            print("No acepto valores negativos")
    else:
        estudiante = [nombre_del_estudiante, matricula,[nota_1, nota_2, nota_3, nota_4]]
        estudiantes.append(estudiante)

        promedio = round(sum(estudiante[2]) / len(estudiante[2]),2)
        estudiante.append(promedio)

for estudiante in estudiantes:
    print(f"Nombre: {estudiante[0]}, Matrícula: {estudiante[1]}, Promedio:{estudiante[3]:.2f}")