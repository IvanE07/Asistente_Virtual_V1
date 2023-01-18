#Librería de números aleatorios
import random

from hablaPython import say

###################################################################################

def valida(numero):
    try:
        int(numero)
        return True
    except ValueError as error:
        print(error)
        return False

###################################################################################

def aleatorio(opcion = 0):
    if opcion == 1:
        numero = random.randint(1, 10)
        say("l El número aleatorio es: " + str(numero))
        print("El número aleatorio es: " + str(numero))

        say("¿Deseas regresar al menú?")
        resp = input("Si/no:\t")

        if resp == "si":
            return True
        else:
            say("Adios Iván")
            print("Ádios!")
            return False

    elif opcion == 2:
        numero = random.randint(1, 6)
        say("l El dado aleatorio es: " + str(numero))
        print("El dado aleatorio es: " + str(numero))

        say("¿Deseas regresar al menú?")
        resp = input("Si/no:\t")

        if resp == "si":
            return True
        else:
            say("Adios Iván")
            print("Ádios!")
            return False

    elif opcion == 3:
        numero = random.randint(1, 1000)
        say("l El número aleatorio es: " + str(numero))
        print("El número aleatorio es: " + str(numero))

        say("¿Deseas regresar al menú?")
        resp = input("Si/no:\t")

        if resp == "si":
            return True
        else:
            say("Adios Iván")
            print("Ádios!")
            return False

    elif opcion == 4:
        numero = 2
        while(numero % 2 == 0):
            numero = random.randint(1, 1000)
        say("El número aleatorio es: " + str(numero))
        print("El número aleatorio es: " + str(numero))

        say("¿Deseas regresar al menú?")
        resp = input("Si/no:\t")

        if resp == "si":
            return True
        else:
            say("Adios Iván")
            print("Ádios!")
            return False

    else:
        say("l No disponible")
        print("No disponible")

###################################################################################

def menu_Aleatorio():
    say("Selecciona tu opción favorita!")
    print("""
    1.- Número del 1 al 10
    2.- Tirar un dado
    3.- Cualquier número aleatorio
    4.- Elige un número impar al azar
    """)

    opc = input("\n")

    if valida(opc):
        if aleatorio(int(opc)):
            return True
        else:
            print(":)")
    else:
        print("\nSolo digita el número de la opción disponible...")

###################################################################################