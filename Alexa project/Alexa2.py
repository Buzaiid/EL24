import speech_recognition as sr
from datetime import *
from time import *
import time
from gtts import *
import pyscreeze
import webbrowser
import playsound
import firelink
import warnings
import random
import sys
import cv2
import os
import pyautogui
import pyjokes
import requests


#Ignore any warninig msg
warnings.filterwarnings('ignore')

class voice_assistant:
    recognizer = sr.Recognizer()

  
    def record_audio(self):
        
        waiting_words=['Listening!','mmm!','What is in your mind','how can i help you?','how can i be of service?']
        random_words=random.choice(waiting_words)
        with sr.Microphone() as source:
            print(random_words)
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
        return audio
    

    def speechRecogntion(self, audio):
        text = " "
        try:
            text = self.recognizer.recognize_google(audio, language="ar-EG")
            print(f"You said: {text}")
        except sr.UnknownValueError:
            print("I am Sorry, i couldn't understand what you said")
        except sr.RequestError:
            print("Sorry, there was a service error.")
            print("Please try again")
        return text
    

    def speak(self, text):
        tts = gTTS(text=text, lang='ar', slow=True)
        tts.save("audio.mp3")
        playsound.playsound("audio.mp3")


    def open_link(self):
        self.speak('اختار الموقع')
        print("Say...")
        audio_data = self.record_audio()
        print("Recognizing speech...")
        text = self.speechRecogntion(audio_data)
        websites = {
            "فيسبوك": firelink.fb,
            "جوجل": firelink.google,
            "يوتيوب": firelink.youtube,
            "سبوتيفاي":firelink.spotify,
            "لينكد أن":firelink.linkedin
        }
        if text in websites:
            url = websites[text]
            firelink.firefox(url)
        else:
            print("Invalid choice. Please try again.")


    def tell_jokes(self):
        joke=pyjokes.get_joke()
        tts=gTTS(text=joke, lang='en')
        tts.save('joke.mp3')
        print(joke)
        playsound.playsound('joke.mp3')
        


    def open_Spotify(self):
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'shift', 't')
        time.sleep(2)
        pyautogui.typewrite("spotify")
        time.sleep(2)
        pyautogui.press("enter")
        time.sleep(15)
        play_icon=pyautogui.locateOnScreen('/home/buzaid/EL24/Alexa project/play_icon.jpg', confidence=0.9)
        play_button_center = pyautogui.center(play_icon)
        pyautogui.click(play_button_center)


    def openCalculator(self):
        time.sleep(2)
        pyautogui.hotkey('shift', 'alt', 'c')


    def getWeather(self):
        api_key='424a4ae3c40fcd238fda7af4b71dd0f0'
        location='Cairo, EG'
        url=f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
        response = requests.get(url)
        if response.status_code==200:
            data=response.json()
            weather = (data['weather'][0]['description'])
            temperature = (data['main']['temp'])
            humidity = (data['main']['humidity'])
            windSpeed = (data['wind']['speed'])
        
            print(f'Current weather in {location}: {weather}')
            self.speak(weather)
            print(f'Temperature: {temperature}°C')
            self.speak('درجة الحرارة')
            self.speak(str(temperature))
            print(f'Humidity: {humidity}%')
            self.speak('الرطوبة')
            self.speak(str(humidity))
            print(f'Wind speed: {windSpeed} m/s')
            self.speak('سرعة الرياح')
            self.speak(str(windSpeed))
        else:
            print('Failed to retrieve weather data.')
            self.speak('في حاجه غلط!')
        

    def get_current_time(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(current_time)
        self.speak(current_time)


    def greeting(self, text):
        goodMornings=['صباح الخير', 'صباح الفل','صباح النور','صباح العسل','صباحووو','صبح صبح']
        goodAfteernoons=['مساء الخير', 'مساء الفل', 'مساء النور','مساءوو','مسا مسا']
        if text in goodMornings:
            random_greetings=random.choice(goodMornings)
            self.speak(random_greetings)
        elif text in goodAfteernoons :
            random_greetings=random.choice(goodAfteernoons)
            self.speak(random_greetings)
        

    def Alexa(self):
        print("Say something...")
        audio_data = self.record_audio()
        print("Recognizing speech...")
        recognized_text = self.speechRecogntion(audio_data)
        if recognized_text in ['صباح الخير', 'صباح الفل', 'مساء الفل''صباح النور', 'مساء الخير']:
            self.greeting(recognized_text)
        elif recognized_text in ["الوقت", "ساعة", "الساعة"]:
            self.get_current_time()
        elif recognized_text in ["الجو", "جو", "درجه الحراره"]:
            self.getWeather()
        elif recognized_text in ['سبوتيفاي','أغاني']:
            self.open_Spotify()
        elif recognized_text in ["موقع","ويب سايت"]:
            self.open_link()
        elif recognized_text in ['ضحك','نكته','comedy']:
            self.tell_jokes()
        elif recognized_text in ['اله','حساب']:
            self.openCalculator()
        elif recognized_text in ["اقفل", "close", "اطفي","سلام","باي باي"]:
            goodBye=['مع السلامه','باي باي','اشوفك غلى خير','تعالى تاني']
            random_Goodbey=random.choice(goodBye)
            self.speak(random_Goodbey)
            sys.exit()


if __name__ == "__main__":
    assistant = voice_assistant()
    while True:
        assistant.Alexa()