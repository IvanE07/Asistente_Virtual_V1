#Busquedas en YouTube
import pywhatkit
#Importar tiempo
from time import sleep

from hablaPython import say

###################################################################################

def reproduce_YouTube():
    anuncio = "Escribe lo qué deseas buscar"
    say(anuncio)
    busqueda = input(anuncio + ":\t")
    anuncio = f"Reproduciendo {busqueda} en YouTube"
    say(anuncio);
    pywhatkit.playonyt(busqueda)

    for x in range(3):
        sleep(1)

    say("¿Deseas regresar al menú?")
    resp = input("Si/no:\t")

    if resp == "si":
        return True
    else:
        say("Adios Iván")
        print("Ádios!")
        return False

###################################################################################

def busca_YT(busqueda):
    anuncio = f"Reproduciendo {busqueda} en YouTube"
    say(anuncio)
    pywhatkit.playonyt(busqueda)

    for x in range(5):
        sleep(1)

    say("¿Deseas regresar al menú?")
    resp = input("Si/no:\t")

    if resp == "si":
        return True
    else:
        say("Adios Iván")
        print("Ádios!")
        return False