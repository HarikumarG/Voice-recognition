import speech_recognition as sr
import sounddevice as sd
from gtts import gTTS
import pygame
r=sr.Recognizer()
mytext="Sir Do you want to activate speech function"
language='en'
myobj=gTTS(text=mytext,lang=language,slow=False)
myobj.save("activate.mp3")
pygame.mixer.init()
pygame.mixer.music.load("activate.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(1)
with sr.Microphone() as source:
    try:
        r.adjust_for_ambient_noise(source)
        print("listening")
        audio=r.listen(source,timeout=5.0)
        print(r.recognize_google(audio))
    except sr.UnknownValueError:
            print("Sorry couldn't understand")    
if "yes" in r.recognize_google(audio):
    mytext="Sir Tell me the first string"
    language='en'
    myobj=gTTS(text=mytext,lang=language,slow=False)
    myobj.save("first_string.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("first_string.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(1)
    with sr.Microphone() as source:
        try:
            r.adjust_for_ambient_noise(source)
            print("listening for first string")
            audio=r.listen(source,timeout=5.0)
            string1=r.recognize_google(audio)
            print(string1)
        except sr.UnknownValueError:
            print("Sorry couldn't understand")
    mytext="Sir Tell me the second string"
    language='en'
    myobj=gTTS(text=mytext,lang=language,slow=False)
    myobj.save("second_string.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("second_string.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(1)
    with sr.Microphone() as source:
        try:
            r.adjust_for_ambient_noise(source)
            print("listening for second string")
            audio=r.listen(source,timeout=5.0)
            string2=r.recognize_google(audio)
            print(string2)
        except sr.UnknownValueError:
            print("Sorry couldn't understand")
    if string1==string2:
        print("equal")
        mytext="Sir they are equal"
        language='en'
        myobj=gTTS(text=mytext,lang=language,slow=False)
        myobj.save("equal_string.mp3")
        pygame.mixer.init()
        pygame.mixer.music.load("equal_string.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(1)
    else:
        print("Not equal")
        mytext="Sir they are not equal"
        language='en'
        myobj=gTTS(text=mytext,lang=language,slow=False)
        myobj.save("not_equal_string.mp3")
        pygame.mixer.init()
        pygame.mixer.music.load("not_equal_string.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(1)
    print("END")



        
        
        
        
        
