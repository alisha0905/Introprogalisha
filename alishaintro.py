vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
nombre = input("Ingrese el nombre: ")
contador = 0
for letra in nombre:
    if letra in vocales:
      contador += 1
      
      
      
if contador >= 3: 
  print("El nombre tiene 3 o mas vocales") 
else:
  print ("El nombre tiene menos de 3 vocales")