

print("Hola, ingresa dos numero de dos digitos")
respuesta1 = int(input("Ingresa el primer numero: "))
respuesta2 = int(input("Ingresa el segundo numero: "))

producto= respuesta1*respuesta2
resta= 0

if 10 <= respuesta1 <= 99 and 10 <= respuesta2 <= 99:
  resta = respuesta1 - respuesta2
else: 
  print("El numero no tiene dos digitos o no cumple con niguna condicion")
  exit()

if resta % 2 == 0:  
  dig=int(respuesta1/10)
  dig2=respuesta1%10
  dig3=int(respuesta2/10)
  dig4=respuesta2%10
  suma= dig+dig2+dig3+dig4

  print("Como la diferencia de los numero es par, la suma de los dos digitos es", suma)

else:
  print('La diferencia de los dos numeros no es par...')


if resta<10 and resta==2 or resta==3 or resta==5 or resta==7:
  print("Como la diferencia de los es primo menor que 10, el producto es",producto)
else:
  print('La diferencia de los dos numeros no es primo menor que 10...')

if str(resta)[-1] == '4':
  digito1=int(respuesta1/10)
  digito2=respuesta1%10
  digito3=int(respuesta2/10)
  digito4=respuesta2%10
  print('La diferencia entre los numeros termina en 4. Los digitos de la resta son:\n',digito1, digito2, digito3, digito4)

