#Habla Python
import pyttsx3
#Entradas por microfóno
import speech_recognition as sr
#Acciones del sistema
import os
#Para esperar segundos
from time import sleep
#Librerías para obtener una contraseña aleatoria
import string, secrets
#Librería para copiar al portapapeles
import pyperclip as clipboard
#Para saber la fecha acttual
import datetime

from youtube import reproduce_YouTube, busca_YT
from inves_Wikipedia import wiki
from num_Aleatorio import menu_Aleatorio
from juegos import menu_Juegos
from traductor import menuTranslator
from speed_Test import velocidad

listener = sr.Recognizer();

nombre = "Iván"

###################################################################################

"""
Programa by Luis Iván Villegas Eligio
Versión: 1
"""

###################################################################################

def say(frase = ""):
    engine = pyttsx3.init()

    #Obtener las voces disponibles
    voices = engine.getProperty('voices')
    #Elegimos la voz 0, correspondiente a la voz de MX
    engine.setProperty('voices', voices[0].id)

    #Dice lo que le mandemos en frase.
    engine.say(frase)
    #Espera un momento y finaliza
    engine.runAndWait()

###################################################################################

def listen():
    rec = "no escuche"
    try:
        with sr.Microphone() as source:

            say("Escuchando")
            print("Escuchando....")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice)
            
            rec = rec.lower()

            return rec
    except:
        pass
    return rec

###################################################################################

def valida(numero):
    try:
        int(numero)
        return True
    except ValueError as error:
        print(error)
        return False

###################################################################################

def password():
    
    say("d Digita el tamaño de la contraseña")
    tamanio = input("Tamaño: \t")

    if valida(tamanio):
        tamanio = int(tamanio)

        password = ""

        contra = string.ascii_letters + string.digits + string.punctuation

        os.system("cls")
        say("Generando contraseña, por favor espera")
        print("Generando....")

        for x in range(4):
            sleep(1)

        os.system("cls")
        say("Contraseña generada con éxito y por seguridad no la mostraré pero la copie al portapapeles")

        for x in range(tamanio):
            password += ''.join(secrets.choice(contra))

        clipboard.copy(password)

        say("¿Deseas regresar al menú?")
        resp = input("Si/no:\t")

        if resp == "si":
            return True
        else:
            say("Adios Iván")
            print("Ádios!")
            return False

    else:
        say("Solo digita números")
        print("Solo digita números....")

###################################################################################

def acciones():

    os.system("cls")

    palabra = listen()

    if palabra == "youtube":
        os.system("cls")

        say("¿Qué deseas reproducir?")
        palabra = listen()

        os.system("cls")

        anuncio = f"Deseas reproducir {palabra}, ¿Es correcto?"
        say(anuncio)
        print(anuncio)

        if listen() == "yes":
            if busca_YT(palabra):
                acciones()
            else:
                print(":)")
        else:
            if reproduce_YouTube():
                acciones()
            else:
                print(":)")


    elif palabra == "buscar":
        os.system("cls")

        say("¿Qué vamos a buscar en wikipedia?")
        palabra = listen()

        os.system("cls")

        anuncio = f"Deseas buscar {palabra}, ¿Es correcto?"
        say(anuncio)
        print(anuncio)

        if listen() == "yes":
            os.system("cls")
            if wiki(palabra):
                acciones()
            else:
                print(":)")
        else:
            os.system("cls")
            say("Escribe lo que vamos a buscar")
            resp = input(":\t")
            anuncio = f"Buscando {resp} en wikipedia"
            if wiki(resp):
                acciones()
            else:
                print(":)")

    elif palabra == "numeros":
        os.system("cls")
        say("Vamos a generar números aleatorios, te mostraré a continuación las opciones")
        if menu_Aleatorio():
            acciones()

    elif palabra == "contrasena":
        os.system("cls")
        say("Vamos a generar una contraseña")
        if password():
            acciones()
        else:
            print(":)")

    elif palabra == "juegos":
        say("Tiempo de divertirnos con algunos juegos")
        if menu_Juegos():
            acciones()

    elif palabra == "traducir":
        say("Es una nueva función que he aprendido!")
        say("solo podemos traducir de ingles a español y viceversa, esperamos en un futuro aprenda otros idiomas")
        os.system("cls")
        if menuTranslator():
            acciones()

    elif palabra in ["speed test", "velocidad internet", "speed", "speed of my internet"]:
        say("Vamos a ver qué tal la velocidad de tu internet y su ping")
        os.system("cls")
        if velocidad():
            acciones()
        else:
            print(":)")

    else:
        anuncio = f"{nombre} no entendí tu palabra, ¿Deseas volver a intentarlo? dí yes ó no"
        say(anuncio)
        respuesta = listen()

        if respuesta == "yes":
            acciones()
        else:
            anuncio = f"Hasta pronto {nombre}! Un placer ayudarte"
            say(anuncio)
            print(":)")

###################################################################################

def hora():
    hora_actual = datetime.datetime.now()

    horas = hora_actual.hour
    minutos = hora_actual.minute
    if (horas >= 5 and horas <= 11):
        return f"Buenos días, son las {horas} con {minutos} minutos de la mañana"
    elif (horas >= 12 and horas <= 18):
        return f"Buenas tardes, son las {horas} con {minutos} minutos de la tarde"
    elif (horas >= 19 and horas <= 23):
        return f"Buenas noches, son las {horas} con {minutos} minutos de la noche"
    else:
        return f"Son las {horas} con {minutos} minutos de la madrugada, ¿Qué haces despierto a esta hora {nombre}?"

###################################################################################

def presentacion():
    say(hora())
    say("Hola Iván, espero estes teniendo un buen día, estoy ansiosa por saber que haremos hoy")
    os.system("cls")
    anuncio = f"{nombre} te muestro lo que podemos hacer hasta ahora"
    say(anuncio)
    print("""
    1.- Reproducir vídeos en youtube
    2.- Buscar en wikipedia
    3.- Números aleatorios
    4.- Generar una contraseña
    5.- Jugar juegos
    6.- Traducir [es to en or en to es]
    7.- Medir velocidad de tu internet
    """)

    print("""\n
    Palabras clave:
    1.- Youtube
    2,. Buscar
    3.- Números
    4.- Contraseña
    5.- Juegos
    6.- Traducir
    7.- Speed test, velocidad internet, speed, speed of my internet
    """)

    say("Puedes decirme la palabra clave de cada oración, así que empecemos, presiona enter cuando estes listo")
    input()
    os.system("cls")
    
    acciones()

###################################################################################

presentacion()