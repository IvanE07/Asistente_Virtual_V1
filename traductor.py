from googletrans import Translator
from hablaPython import say
from os import system

traducir = Translator()

def traduce(sentence = "", bandera = 4):
    if bandera == 0:
        try:
            traduce = traducir.translate(sentence, dest = 'es')
            anuncio = f"{sentence} en español se dice {traduce.text}"
            say(anuncio)
            print(traduce.text)

            say("¿Deseas regresar al menú?")
            resp = input("Si/no:\t")

            if resp == "si":
                return True
            else:
                say("Adios Iván")
                print("Ádios!")
                return False

        except AttributeError as error:
            print(error)
    elif bandera == 1:
        try:
            traduce = traducir.translate(sentence, dest = 'en')
            anuncio = f"{sentence} en inglés se dice {traduce.text}"
            say(anuncio)
            print(traduce.text)

            say("¿Deseas regresar al menú?")
            resp = input("Si/no:\t")

            if resp == "si":
                return True
            else:
                say("Adios Iván")
                print("Ádios!")
                return False

        except AttributeError as error:
            print(error)
    else:
        print("Opción desconocida o no has escrito correctamente")

def menuTranslator():

    system("cls")

    say("Selecciona la opción para traducir")
    print("""
    1.- English to Spanish
    2.- Spanish to English
    3.- Exit
    """)
    opc = input("Write your option:\t")

    if opc in ["1", "uno", "one"]:
        say("Escribe la oración")
        sentence = input("Write your sentence:\t")
        if traduce(sentence, 0):
            return True
        else:
            print(":)")
    elif opc in ["2", "dos", "two"]:
        say("Escribe la oración")
        sentence = input("Escribe la oración:\t")
        if traduce(sentence, 1):
            return True
        else:
            print(":)")
    elif opc in ["3", "tres", "three"]:
        say("Hasta pronto usuario, un placer ayudarte!")
        print("Goodbye!!!")
    else:
        print(f"Option {opc} unkown, try again")
        input("Enter")
        menuTranslator()