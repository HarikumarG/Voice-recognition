import speech_recognition as sr
from gtts import gTTS
import pygame
import smtplib
from selenium import webdriver
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
            audio=r.listen(source,timeout=3.0)
            print(r.recognize_google(audio))
            value=r.recognize_google(audio)
        except sr.UnknownValueError:
            print("sorry couldn't understand")
            value="sorry couldn't understand"
        return value
def mailsend():
    text_to_speech("Sir Do you want to activate mail","activate.mp3")
    content=speech_to_text()
    if "yes" in content:
        text_to_speech('who is the recipient',"recipient.mp3")
        content=speech_to_text()
        if "any unique name to activate this block" in content:
            text_to_speech("what should i send in your message sir ?","question.mp3")
            content=speech_to_text()
            mail=smtplib.SMTP('smtp.gmail.com',587)
            mail.ehlo()
            mail.starttls()
            mail.login('sender emailid','yourpassword')
            mail.sendmail('subject','receiver mail id',content)
            mail.close()
            text_to_speech("email sent","sent.mp3")
    print("END")
def fblogin():
    text_to_speech("Sir Do you want to login into face book ?","activate.mp3")
    content=speech_to_text()
    if "yes" in content:
        driver = webdriver.Firefox(executable_path="C:\\Users\\Harikumar G\\Downloads\\Firefox driver\\geckodriver.exe")
        driver.get('https://www.facebook.com/')
        username_box = driver.find_element_by_id('email')
        username_box.send_keys('email id')
        password_box = driver.find_element_by_id('pass')
        password_box.send_keys('password')
        login_box = driver.find_element_by_id('loginbutton')
        login_box.click()
        text_to_speech("Sir logged in successfully","log.mp3")
    print("END")
text_to_speech("Sir which function you would like to activate ? mail send or facebook login","start.mp3")
content=speech_to_text()
if "mail" in content:
    mailsend()
elif "Facebook" in content:
    fblogin()
else:
    text_to_speech("sorry sir couldn't understand","sorry.mp3")
print("END")
    
    
