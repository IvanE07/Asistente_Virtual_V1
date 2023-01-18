#Libreria para esperar segundos
from time import sleep
#Librería de números aleatorios
import random
#Para limpiar pantalla
from os import system

from hablaPython import say
from variables import adivina, word_User, respTF

###################################################################################

def bola_Magica():
    
    system("cls")

    say("La bola de Cristal está lista para responder si o no a tu pregunta.")
    say("Piensa tu pregunta en")
    
    i = 3

    while(i >= 1):
        say(str(i))
        i -= 1
    say("Dime tu pregunta")
    pregunta = input(":\t")

    say("La respuesta está en camino...")
    say("sobre si o no" + pregunta)
    say("La respuesta es....")
    sleep(1)

    resp_Aleatorio = random.choice(respTF)
    say(resp_Aleatorio)
    print(resp_Aleatorio)

    say("¿Deseas regresar al menú?")
    resp = input("Si/no:\t")

    if resp == "si":
        return True
    else:
        say("Adios Iván")
        print("Ádios!")
        return False

###################################################################################

def el_Ahorcado():
        
    system("cls")
    
    say("¿Alguna vez haz jugado a el ahorcado?")
    say("Tienes que adivinar una palabra aleatoria, tienes 5 intentos, vamos a empezar!")
    system("cls")

    palabras = open("palabras.txt", mode = "r")
    intentos = 2
    limite = 6
    i = 0
    
    for palabra in palabras:
        palabra = palabra.rstrip().lower()
        adivina.append(palabra)

    palabras.close()

    palabra = random.choice(adivina)

    for i in range(len(palabra)):
        word_User.append("_")


    system("cls")
    anuncio = f"Tamaño de la palabra: {len(palabra)}"
    say(anuncio)
    print(anuncio, "\n")
    
    anuncio = f"Cuentas con {limite - 1} intentos para adivinar la palabra"
    say(anuncio)
    print(anuncio)
    input("Presiona enter para aceptar\t")

    system("cls")

    while(intentos <= limite):    

        say("Digita una letra")
        letter = input("Digita una letra: \t")

        i = 0

        for letras in palabra:
            if letter == letras:
                word_User[i] = letter
            
            else:
                if word_User[i] != "_":
                    pass
                else:
                    word_User[i] = "_"

            i += 1

        print("\n", word_User)

        say("¿Ya sabes la palabra?")
        respuesta = input("¿Ya sabes la palabra? si/no\t")

        if respuesta == "si" or respuesta == "s":
            system("cls")
            print("\n", word_User)
            say("Escribre la palabra")
            respuesta = input("Digita la palabra: \t")

            if respuesta == palabra:
                say("Felicidades, haz ganado")
                print(f"Felicidades! Ganaste")
                break

            else:
                anuncio = f"Perdiste el muñequito ha muerto ahorcado, la palabra era {palabra}. Estoy triste"
                say(anuncio)
                print(anuncio)
                break

        else:
            system("cls")
            print("\n", word_User)
        anuncio = f"Tienes {limite - intentos} intentos"
        say(anuncio)
        print(anuncio)
        
        intentos += 1

    if intentos == 7:
        system("cls")
        anuncio = "Última oportunidad para adivinar la palabra"
        say(anuncio)
        print(anuncio)
        print("\n", word_User)

        anuncio = "Escribe la palabra"
        say(anuncio)
        respuesta = input("Digita la palabra: \t")

        if respuesta == palabra:
            say("Felicidades, haz ganado")
            print(f"Felicidades! Ganaste")

        else:
            anuncio = f"Perdiste el muñequito ha muerto ahorcado, la palabra era {palabra}. Estoy triste"
            say(anuncio)
            print(anuncio)

    say("¿Deseas regresar al menú?")
    resp = input("Si/no:\t")

    if resp == "si":
        return True
    else:
        say("Adios Iván")
        print("Ádios!")
        return False

###################################################################################

def cien_Puntos():
        
    system("cls")

    player1 = 0
    player2 = 0
    acumulador = 0
    acumulador2 = 0

    say("Escribe tu nombre jugador 1")
    name_Player1 = input("¿Cómo te llamas?\t")

    system("cls")

    say("Escribe tu nombre jugador 2")
    name_Player2 = input("¿Cómo te llamas?\t")

    system("cls")

    while (player1 < 50 and player2 < 50):
                
        acumulador = random.randint(1, 6)
        player1 += acumulador
        anuncio = f"{name_Player1} obtuvo " + str(acumulador) + " puntos"
        say(anuncio)

        acumulador2 = random.randint(1, 6)
        player2 += acumulador2
        anuncio = f"{name_Player2} obtuvo " + str(acumulador2) + " puntos"
        say(anuncio)
        
        system("cls")
        print(f"\n{name_Player1}: {player1} puntos vs {name_Player2}: {player2} puntos")

        if player1 > 50:
            say(f"{name_Player1} Rebaso los 50 puntos, se le restaran los puntos obtenidos")
            system("cls")
            player1 -= acumulador
            print(f"\n{name_Player1}: {player1} puntos vs {name_Player2}: {player2} puntos")

        if player2 > 50:
            say(f"{name_Player2} Rebaso los 50 puntos, se le restaran los puntos obtenidos")
            system("cls")
            player2 -= acumulador2
            print(f"\n{name_Player1}: {player1} puntos vs {name_Player2}: {player2} puntos")

        sleep(1)

    
    if player1 > player2:
        anuncio = f"Gana {name_Player1} con {player1} puntos a {name_Player2} con {player2} puntos"
        say(anuncio)
        print(anuncio)
    elif player2 > player1:
        anuncio = f"Gana {name_Player2} con {player2} puntos a {name_Player1} con {player1} puntos"
        say(anuncio)
        print(anuncio)
    else:
        anuncio = "Empate!!!, ambos tuvieron 100 puntos!!!!, pero debe haber un ganador, así que ambos tiraran nuevamente el dado"
        say(anuncio)
        anuncio = "El que obtenga el número mayor ganará"

        acumulador2 = 1
        acumulador = 1

        while (acumulador == acumulador2):
            acumulador = random.randint(1, 6)
            acumulador2 = random.randint(1, 6)

        if acumulador > acumulador2:
            anuncio = f"Gana {name_Player1} obteniendo {acumulador} puntos a {name_Player2} que obtuvo {acumulador2} puntos"
            say(anuncio)
            print(anuncio)
        else:
            anuncio = f"Gana {name_Player2} obteniendo {acumulador2} puntos a {name_Player1} que obtuvo {acumulador2} puntos"
            say(anuncio)
            print(anuncio)

        print(anuncio)

    say("¿Deseas regresar al menú?")
    resp = input("Si/no:\t")

    if resp == "si":
        return True
    else:
        say("Adios Iván")
        print("Ádios!")
        return False

###################################################################################

def menu_Juegos():
    
    system("cls")

    say("¿Qué deseas jugar? Tengo estos tres juegos")

    print("""
    1.- 50 Puntos (2 jugadores)
    2.- El Ahorcado
    3.- Bola Mágica
    """)

    opc = input("Selecciona una opción: \t")

    if opc == "1":
        if cien_Puntos():
            return True
    elif opc == "2":
        if el_Ahorcado():
            return True
    elif opc == "3":
        if bola_Magica():
            return True
    else:
        say("Opción no reconocida, vuelve a intentarlo, presiona enter")
        input()
        menu_Juegos()

###################################################################################