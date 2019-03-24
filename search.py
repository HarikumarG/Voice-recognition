import speech_recognition as sr
import webbrowser
from gtts import gTTS
import pygame
def text_to_speech(content,file):
    mytext=content
    language='en'
    myobj=gTTS(text=mytext,lang=language,slow=False)
    myobj.save(file)
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(1)
def speech_to_text():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        try:
            r.adjust_for_ambient_noise(source)
            print("listening")
            audio=r.listen(source,timeout=5.0)
            print(r.recognize_google(audio))
            value=r.recognize_google(audio)
        except sr.UnknownValueError:
            print("sorry couldn't understand")
            value="sorry couldn't understand"
        return value
def search():
    text_to_speech("Sir tell me what do you want to search in wikipedia","wiki.mp3")
    content=speech_to_text()
    url="https://en.wikipedia.org/wiki/"
    try:
        webbrowser.open_new(url+content)
    except sr.RequestError as e:
        print("Failed to retrieve results".format(e))
text_to_speech("Sir do you want to activate google search","start.mp3")
content=speech_to_text()
if "search" in content:
    search()            
