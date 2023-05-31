import pyttsx3

def obtener_texto():
    text = input("Ingresa el texto: ")
    return text

def convertir_a_voz(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

text = obtener_texto()
convertir_a_voz(text)