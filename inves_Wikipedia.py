#Librería para buscar en wikipedia
import wikipedia

from hablaPython import say

###################################################################################

def wiki(busqueda):
    try:        
        wikipedia.set_lang('es')        
        print(wikipedia.summary(busqueda))
        resena = wikipedia.summary(busqueda, sentences = 1)
        say("Esto es lo que encontré referente a " + busqueda)
        say(resena)

        say("¿Deseas regresar al menú?")
        resp = input("Si/no:\t")

        if resp == "si":
            return True
        else:
            say("Adios Iván")
            print("Ádios!")
            return False

    except wikipedia.PageError as error:
        print(f"\nError por: {error}")
        say("Ha ocurrido un error, redirigiendo al menú")
        return True

###################################################################################