#Ejercicio 1
#Definir un programa que decida quién es el ganador en un juego de Piedra, Papel o Tijera. 

"""jugador1 = input("¿Cuál es la jugada del primer jugador? ")
jugador2 = input("¿Cuál es la jugada del segundo jugador? ")

if jugador1 == jugador2:
    print("Hubo empate")
elif jugador1 == "piedra":
  
    if jugador2 == "papel":
        print("Gano el segundo jugador")
    else:
        print("Gano el primer jugador")
elif jugador1 == "papel":
    if jugador2 == "tijera":
        print("Gano el segundo jugador")
    else:
        print("Gano el primer jugador")
elif jugador1 == "tijera":
    if jugador2 == "piedra":
        print("Gano el segundo jugador")
    else:
        print("Gano el primer jugador")
else:
    print("Respuesta invalida. Por favor elija piedra, papel o tijera.")"""


#Ejercicio 2
#Definir un programa que reciba 5 números enteros y luego muestre cuál de los valores ingresados fue el mayor.

"""numeros = []
for i in range(5):
  numero = int(input("Ingrese un número: "))
  numeros.append(numero)

mayor = numeros[0]
for i in range(1, 5):
    if numeros[i] > mayor:
        mayor = numeros[i]

print("El número mayor es:", mayor)"""




#Ejercicio 3
#Definir un programa que reciba números enteros y luego muestre cuál es la suma de los números pares. 

"""num_pares = 0
while True:
  ingreso = int(input("Ingrese un numero: "))
  
  if int(ingreso) % 2 == 0:
    num_pares += int(ingreso)

  pregunta = input("Desea ingresar otro? ")
  if pregunta == "no":
    break

print("La suma de los números pares es: ", num_pares)"""


#Ejercicio 4
#Crear un programa que permita a un usuario adivinar un número secreto entre 1 y 100.

"""intentos = 0
numero_secreto = int(input("Jugador 1: Ingrese un numero: "))
while True:
  respuesta = int(input("Jugador 2: Ingrese un numero: "))

  if numero_secreto < respuesta:
    intentos = intentos + 1
    print("El número secreto es mas chico. Intente nuevamente")

  elif numero_secreto > respuesta:
    intentos = intentos + 1
    print("El número secreto es mas grande. Intente nuevamente")

  if numero_secreto == respuesta:
    intentos = intentos + 1 
    print("Acertó el número secreto. " "Usó", intentos,"intentos para adivinar" )

    break"""


#Ejercicio 6
#Escribe un programa que te permita jugar a una versión simplificada del juego Código Oculto. El juego consiste enadivinar una cadena de 4 números distintos. El usuario debe ingresar números hasta adivinar la cadena de números y tiene 8 intentos para adivinar.



#correccion de clase


contador_acierto = 0
codigo_lista = []
adivinar_lista = []
contador_intentos = 0

ingreso_codigo = input("Ingrese el código secreto: ")

for i in ingreso_codigo:
  codigo_lista.append(ingreso_codigo[i])

while (contador_intentos < 8):
  
  adivinar = input("Ingrese el número con el que quiere adivinar el código secreto")
  for i in range(len(adivinar)):
    adivinar_lista.append(adivinar[i])
  
  for i in range(len(ingreso_codigo)):
    if (ingreso_codigo[i] == adivinar_lista[i]):
      contador_acierto = contador_acierto + 1

  print("Usted tuvo ", contador_acierto, " aciertos")
  print("Le quedan ", contador_intentos, " intentos")

  
  contador_intentos = contador_intentos + 1
  


  







   





    
  




  

  
  

  
    
    
  
  
  
  
