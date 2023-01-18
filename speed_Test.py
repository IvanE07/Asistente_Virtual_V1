import speedtest
from os import system

from hablaPython import say

#######################################################################

test = speedtest.Speedtest()
system("cls")

#######################################################################

def velocidad():
    say("Cargando lista de servidores, por favor espera")
    print("Cargando lista de servidores...")
    test.get_servers() #Obetener una lista de servidores

    say("Eligiendo el mejor servidor")
    print("Eligiendo el mejor servidor...")
    best = test.get_best_server() #Obtener el mejor servidor para tener un resultado óptimo

    system("cls")

    anuncio = f"Servidor encontrado: nombre: {best['host']} localizado en: {best['country']} por: {best['sponsor']}"
    say(anuncio)
    print(anuncio) #Imprimimos datos relevantes

    say("Obteniendo información de descarga")
    print("\nObteniendo información de descarga...")
    descarga = test.download()

    say("Obteniendo información de subida")
    print("\nObteniendo información de subida...")
    subida = test.upload()

    ping = test.results.ping

    anuncio = f"Tu ping es de: {ping:.2f} ms"
    say(anuncio)
    print("\n" + anuncio)
    
    descarga = descarga / 1024 / 1024
    subida = subida / 1024 / 1024

    anuncio = f"Descarga: {descarga:.2f}Mb.      Subida: {subida:.2f}Mb."
    say(anuncio)
    print(anuncio)

    if descarga >= 0 and descarga <= 10:
        say("Tu velocidad de bastante baja, solo para redes sociales y ver contenido multimedia en calidad estandar o 480p")
    elif descarga >= 11 and descarga <= 50:
        say("Tu velocidad es buena para descargar grandes archivos y ver contenido multimedia en full hd y hasta 4k")
    elif descarga > 50:
        say("Tu velocidad es impresionante, todo se realiza en momentos instantaneos, puedes hacer cualquier cosa en cuestión de segundos")

    
    say("¿Deseas regresar al menú?")
    resp = input("Si/no:\t")

    if resp == "si":
        return True
    else:
        say("Adios Iván")
        print("Ádios!")
        return False


#######################################################################