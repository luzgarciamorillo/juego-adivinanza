import random
numero_secreto = random.randint (0, 100) #Acordarse que randint es para número random entero.
adivinado = False

print("¡Bienvenido al juego de adivinar el número secreto")

while not adivinado: 
    entrada = input("Introduce un numero del 1 al 99: ") # TO DO: convenrtir a número
    numero = int(entrada)
    if numero == numero_secreto:
        print("¡Felicitaciones has adivinado el número secreto!")
        adivinado = True
    elif numero < numero_secreto:
        print("El número es mayor al ingresado")
    else:
        print("El número es menor al ingresado")

# Puedo complejizarlo
numero_secreto = random.randint (0, 100) #Acordarse que randint es para número random entero.
cant_intentos = 0
cant_max_intentos = 5
adivinado = False

print("¡Bienvenido al juego de adivinar el número secreto")

while not adivinado and cant_intentos < cant_max_intentos: 
    entrada = input("Introduce un numero del 1 al 99: ") # TO DO: convenrtir a número
    numero = int(entrada)
    if numero == numero_secreto:
        print("¡Felicitaciones has adivinado el número secreto!")
        adivinado = True
    elif numero < numero_secreto:
        print("El número es mayor al ingresado")
    else:
        print("El número es menor al ingresado")
    cant_intentos += 1
if not cant_intentos < cant_max_intentos:
    print("¡Game Over! No has logrado adivinar en la cantidad de intentos")

# Otra manera 
while not adivinado: 
    if not cant_intentos < cant_max_intentos:
        print("¡Game Over! No has logrado adivinar en la cantidad de intentos")
        break
    entrada = input("Introduce un numero del 1 al 99: ") # TO DO: convenrtir a número
    numero = int(entrada)
    if numero == numero_secreto:
        print("¡Felicitaciones has adivinado el número secreto!")
        adivinado = True
    elif numero < numero_secreto:
        print("El número es mayor al ingresado")
    else:
        print("El número es menor al ingresado")
    cant_intentos += 1