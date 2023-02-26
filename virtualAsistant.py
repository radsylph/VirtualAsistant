import speech_recognition as sr
import pyttsx3 as IA
import pywhatkit
import datetime
import webbrowser
from playsound import playsound
import wikipedia

wikipedia.set_lang('es')

#function to convert text to speech using the speech_recognition library
listener = sr.Recognizer()
#function to convert speech to text using the pyttsx3 library
engine = IA.init()

#array with the selected languages
idiom = ['es-ES', 'en-US']
moth = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
position = 0
position2 = 0
name = 'alexa'
loop = True

IA = IA.init()
voices = IA.getProperty('voices')
IA.setProperty('voice', voices[position2].id)
IA.setProperty('rate', 140)


def talk(text):
    engine.say(text)
    engine.runAndWait()

playsound(r"C:\Users\Usuario\Desktop\basura 2\repo\AlexaIA\asistente\start.mp3")

if position ==0:
    talk("bienvenido, en que puedo ayudarte hoy ?")
elif position == 1:
    talk("welcome, what can I do for you today ?")
while loop == True:
 try:
  recognizer = sr.Recognizer()
  with sr.Microphone() as source:
    if position == 0:
        print("Escuchando...")
        talk("Escuchando...")
    elif position == 1:
        print("Listening...")
        talk("Listening...")
    audio = recognizer.listen(source , phrase_time_limit=5)
    command = recognizer.recognize_google(audio , language = idiom[position])
    command = command.lower()
    command = command.split(' ')

    if 'kermit' in command:
            playsound(r"C:\Users\Usuario\Desktop\basura 2\repo\AlexaIA\asistente\borzoing.mp3")
    elif 'crazy' in command:
            playsound(r"C:\Users\Usuario\Desktop\basura 2\repo\AlexaIA\asistente\crazy.mp3")
    elif 'saber' in command:
            playsound(r"C:\Users\Usuario\Desktop\basura 2\repo\AlexaIA\asistente\excalibur.mp3")
    if position == 0:
        if name in command:
            if 'reproduce' in command:
                    talk('reproduciendo')
                    print(command)
                    pywhatkit.playonyt(command)
            elif 'busca' in command:
                    talk('buscando')
                    print(command)
                    command.remove('alexa')
                    command.replace("busca" , '')
                    command = ' '.join(command)
                    pywhatkit.search(command)
            elif 'cambiar idioma' in command or "cambia de idioma" in command or "ingles" in command:
                    position = 1
                    position2 = 2
                    talk("cambiando idioma a ingles")
            elif 'abre' in command or 'abrir' in command:
                    sites = {
                        'youtube': 'https://www.youtube.com/',
                        'google': 'https://www.google.com/',
                        'facebook': 'https://www.facebook.com/',
                        'instagram': 'https://www.instagram.com/',
                        'twitter': 'https://twitter.com/',
                        'gmail': 'https://mail.google.com/mail/u/0/#inbox',
                        'whatsapp': 'https://web.whatsapp.com/',
                        'telegram': 'https://web.telegram.org/',
                        'wikipedia': "https://es.wikipedia.org/wiki/Wikipedia:Portada",
                    }
                    for i in list(sites.keys()):
                        if i in command:
                            webbrowser.open(sites[i])
                            talk("abriendo" + i)
            elif 'hora' in command:
                    time = datetime.datetime.now().strftime('%H:%M')
                    talk('Son las' + time)
            elif 'fecha' in command:
                    date = datetime.datetime.now().strftime('%d/%m/%Y')
                    moth = datetime.datetime.now().strftime('%m')
                    moth = int(moth)-1
                    for mes in meses:
                        if moth == meses.index(mes):
                            moth = mes
                    fecha = date.split('/')
                    fecha2 = fecha[0] + ' de ' + moth + ' del ' + fecha[2]
                    print(moth)
                    talk('Hoy es' + fecha2)
            elif 'idioma' in command or "cambia de idioma" in command:
                    if position == 0:
                        position = 1
                        talk("cambiando idioma a ingles")
                    elif position == 1:
                        position = 0
                        talk("cambiando idioma a español")
            for i in ["termina" , "apagar" , "adios" , "cierra" , "apaga" , "cerrar" , "adios"]:
                    if i in command:
                        talk("Hasta luego")
                        loop = False
                        break

    elif position == 1:
        
            if 'play' in command:
                    talk('playing')
                    print(command)
                    pywhatkit.playonyt(command)
            if 'hello' in command:
                    talk("hi how are you ? I hope you are feeling good")
            elif 'search' in command:
                    talk('searching')
                    print(command)
                    command.remove('search')
                    command = ' '.join(command)
                    pywhatkit.search(command)
            elif 'change language' in command or "language" in command or "spanish" in command:
                    position = 0
                    position2 = 0
                    talk("changing language to spanish")
            elif 'open' in command:
                    sites = {
                        'youtube': 'https://www.youtube.com/',
                        'google': 'https://www.google.com/',
                        'facebook': 'https://www.facebook.com/',
                        'instagram': 'https://www.instagram.com/',
                        'twitter': 'https://twitter.com/',
                        'gmail': 'https://mail.google.com/mail/u/0/#inbox',
                        'whatsapp': 'https://web.whatsapp.com/',
                        'telegram': 'https://web.telegram.org/',
                        'wikipedia': "https://es.wikipedia.org/wiki/Wikipedia:Portada",
                    }
                    for i in list(sites.keys()):
                        if i in command:
                            webbrowser.open(sites[i])
                            talk("opening" + i)
            elif 'time' in command:
                    time = datetime.datetime.now().strftime('%H:%M')
                    talk('It is' + time)
            elif 'day' in command or "date" in command:
                    date = datetime.datetime.now().strftime('%d/%m/%Y')
                    moth = datetime.datetime.now().strftime('%m')
                    moth = int(moth)-1
                    for mes in moth:
                        if moth == moth.index(mes):
                            moth = mes
                    fecha = date.split('/')
                    fecha2 = fecha[0] + ' of ' + moth + ' of ' + fecha[2]
                    print(moth)
                    talk('Today is' + fecha2)
            for i in ["end" , "turn off" , "bye" , "end" , "turn off" , "close" , "bye"]:
                    if i in command:
                        talk("Bye")
                        loop = False
                        break
 except:
    if position == 0:
        talk("No te entendi, puedes repetirlo?")
    elif position == 1:
        talk("I didn't understand you, can you repeat it?")

