#Habla Python
import pyttsx3

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