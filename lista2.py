numeros = []
for i in range(5):
    numero = int(input("Ingresa un número entero: "))
    numeros.append(numero)

# Calcular la suma de los números pares
suma_pares = 0
for numero in numeros:
    if numero % 2 == 0:
        suma_pares += numero

print("La suma de los números pares es:", suma_pares)