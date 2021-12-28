import pyttsx3#installing pywin is mandatory
from datetime import *
import speech_recognition as hear
import time#for getting current time
import calendar#for using date functions
import smtplib#for sending mail
import wikipedia#for wikipedia information
from plyer import notification
import webbrowser
import webbrowser as wb#for browsing or surfing on internet
wb. register('chrome', None)
import os#for using music file directory
import pyaudio

#installation of pipwin is necessary

engine = pyttsx3.init('sapi5')#for voice synthesis
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[0].id)

def speak(sentence):
    engine.say(sentence)
    engine.runAndWait()

def greetMe():
    hr=int(datetime.now().hour)
    if hr>=0 and hr<=12:
        notifyme('Good Morning Saurabh')
        speak('Good Morning Saurabh')

    elif hr>=12 and hr<=17:
        notifyme('Good Afternoon')
        speak('Good Afternoon Saurabh')

    else:
        notifyme('Good Evening Saurabh')
        speak('Good Evening Saurabh')


    speak('I am your loyal assistant')

def weeday():
    to = date.today()
    born = datetime.weekday(to)
    return calendar.day_name[born]

def schedule():
    day = weeday()
    speak(f'Yor schedule for today {day} is mentiond below in the output screen')

    if day=='Monday' or day=='monday':
        print('===========Monday===========')
        time.sleep(2)
        print('From 9 A.M. to 10 A.M. you have Computer networks class by Madvi Bera mam')
        speak('From 9 A.M. to 10 A.M. you have Computer networks class by Madvi Bera mam')
        time.sleep(2)
        print('From 10 10 A.M. to 11 10 A.M. you have Open Elective class by Jainisha Patel mam')
        speak('From 10 10 A.M. to 11 10 A.M. you have Open Elective class by Jainisha Patel mam')
        time.sleep(2)
        print('From 11 10 A.M. to 12 10 P.M. you have Web Technology class by Hiren Mer sir')
        speak('From 11 10 A.M. to 12 10 P.M. you have Web Technology class by Hiren Mer sir')
        time.sleep(2)
        print('From 12 20 P.M. to 1 20 P.M. you have Problem For Scientific Computing class   by Bhumi Shah mam')
        speak('From 12 20 P.M. to 1 20 P.M. you have Problem For Scientific Computing class   by Bhumi Shah mam')
        time.sleep(2)
        print('From 1 20 P.M. to 2 P.M. you have Lunch break')
        speak('From 1 20 P.M. to 2 P.M. you have Lunch break')
        speak('Your Menu for Monday is Indain Dal rice with 4 chapatti and bhindi sabji')
    if day=='Tuesday' or day=='tuesday':
        print('===========Tuesday===========')
        print('9 A.M. to 10 A.M. Problem For Scientific Computing class   by Bhumi Shah mam')
        speak('From 9 A.M. to 10 A.M. you have Problem For Scientific Computing class   by Bhumi Shah mam')
        time.sleep(2)
        print('10 10 A.M. to 11 10 A.M.  Web Technology class by Hiren Mer Sir')
        speak('From 10 10 A.M. to 11 10 A.M. Web Technology class by Hiren Mer Sir')
        time.sleep(2)
        print(' 11 10 A.M. to 12 10 P.M.  Computer Networks class by Madhvi Bera mam')
        speak('From 11 10 A.M. to 12 10 P.M. you have Computer Networks class by Madhvi Bera mam')
        time.sleep(2)
        print('12 20 P.M. to 1 20 P.M.  Microprocessor And Interfacing class   by Hinal Shah mam')
        speak(' 12 20 P.M. to 1 20 P.M. Microprocessor And Interfacing class   by Hinal Shah ')
        time.sleep(2)
        print('1 20 P.M. to 2 P.M. Lunch break')
        speak('From 1 20 P.M. to 2 P.M. you have Lunch break')
        speak('Your Menu for Tuesday is Italian Pasta')
    if day=='Wednesday' or day=='wednesday':
        print('===========Wednesday===========')
        print('On Wednesday you have offline Labs in the college itself.')
        print('So,you are required to remain present in the college itself')
        print("During Lunch Break you usually prefer to eat Canteen's food.")
        print('I believe cheese puff is your favourite')
        speak('On Wednesday you have offline Labs in the college itself.')
        speak('So,you are required to remain present in the college itself')
        speak("During Lunch Break you usually prefer to eat Canteen's food.")
        speak('I believe cheese puff is your favourite')
    if day=='Thursday' or day=='thursday':
        print('===========Thursday===========')
        print('9 A.M. to 10 A.M. Problem For Scientific Computing class   by Bhumi Shah mam')
        speak('From 9 A.M. to 10 A.M. you have Problem For Scientific Computing class   by Bhumi Shah mam')
        time.sleep(2)
        print('10 10 A.M. to 11 10 A.M.  Web Technology class by Hiren Mer Sir')
        speak('From 10 10 A.M. to 11 10 A.M. Web Technology class by Hiren Mer Sir')
        time.sleep(2)
        print(' 11 10 A.M. to 12 10 P.M.  Computer Networks class by Madhvi Bera mam')
        speak('From 11 10 A.M. to 12 10 P.M. you have Computer Networks class by Madhvi Bera mam')
        time.sleep(2)
        print('12 20 P.M. to 1 20 P.M.  Microprocessor And Interfacing class   by Hinal Shah mam')
        speak(' 12 20 P.M. to 1 20 P.M. Microprocessor And Interfacing class   by Hinal Shah ')
        time.sleep(2)
        print('1 20 P.M. to 2 P.M. Lunch break')
        speak('From 1 20 P.M. to 2 P.M. you have Lunch break')
        speak('Your Menu for Tuesday is Italian Pasta')
    if day=='Friday' or day=='friday':
        print('===========Friday===========')
        print('9 A.M. to 10 A.M. Problem For Scientific Computing class   by Bhumi Shah mam')
        speak('From 9 A.M. to 10 A.M. you have Problem For Scientific Computing class   by Bhumi Shah mam')
        time.sleep(2)
        print('10 10 A.M. to 11 10 A.M.  Web Technology class by Hiren Mer Sir')
        speak('From 10 10 A.M. to 11 10 A.M. Web Technology class by Hiren Mer Sir')
        time.sleep(2)
        print(' 11 10 A.M. to 12 10 P.M.  Computer Networks class by Madhvi Bera mam')
        speak('From 11 10 A.M. to 12 10 P.M. you have Computer Networks class by Madhvi Bera mam')
        time.sleep(2)
        print('12 20 P.M. to 1 20 P.M.  Microprocessor And Interfacing class   by Hinal Shah mam')
        speak(' 12 20 P.M. to 1 20 P.M. Microprocessor And Interfacing class   by Hinal Shah ')
        time.sleep(2)
        print('1 20 P.M. to 2 P.M. Lunch break')
        speak('From 1 20 P.M. to 2 P.M. you have Lunch break')
        speak('Your Menu for Tuesday is Italian Pasta')
def wiki():
    word=input('Enter what you are looking for:-')
    time.sleep(3)
    speak('Loading............\n')
    print('looking into wikipedia........\n')
    speak('looking into wikipedia........')
    results=wikipedia.summary(word,sentences=2)
    print('according to wikipedia....\n')
    speak('according to wikipedia....')
    print(results)
    speak(results)

def sendmail():#Hide password
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your username','password')
    server.sendmail('username of person whom you want to send mail','pandyavedant2205@gmail.com','This message has been'
                                                                                               ' sent from python console')
    server.close()
# def talk():
#     r=hear.Recognizer()
#
#
#     with hear.Microphone() as source:
#         print('Listening.............')
#         r.pause_threshold = 1
#         audio=r.listen(source)
#
#         try:
#             print('Recognizing.......')
#             sentence =r.recognize_google(audio,'en-in')
#             print(f'User Said {sentence}')
#         except Exception as e:
#             print('Say that agin please!!')
#             return 'None'
#         return sentence

def readdiary():
    with open('Diary.txt','r') as re:
        data=re.readlines()
        for li in data:
            print(li)
            speak(li)
    re.close()
def youtube():
    str = input('Enter what you want to see in youtube:')
    time.sleep(4)
    print('Loading.........')
    time.sleep(4)
    wb.open(f'https://www.youtube.com/results?search_query={str}/')
def openmeet():
    notification.notify(
        title='Entering into class',
        message="Let's stydy ",
        # app_icon="C:\\Users\\Krishna\\Downloads\\google_assistant_icon-icons.com_61478\.ico",
        # displaying time
        timeout=3
    )
    wb.open('https://meet.google.com/vvk-cpeg-pbt?pli=1&authuser=1')
def listenmusic():
    music_dir = 'H:\\videos'
    songs = os.listdir(music_dir)
    print(songs)
    os.startfile(os.path.join(music_dir, songs[0]))

def notifyme(msg):
    notification.notify(
        title=msg,
        message="Welcome , I am your assistant ",
        # app_icon="C:\\Users\\Krishna\\Downloads\\google_assistant_icon-icons.com_61478\.ico",
        # displaying time
        timeout=3
    )

def services():
    print('==========Services==========')
    print('1)Schedule')
    print('2)Search In Wiki')
    print('3)Youtube for entertainment')
    print('4)Go to classroom to study')
    print('5)Send Mail')
    print('6)Read Diary')
    print('7)Listen Music')
    print('8)Exit from the system')

if __name__ == '__main__':

    greetMe()
    # while True:
    #     sentence = talk().lower()
    #
    #     if 'hello' in sentence:
    #         speak('hello')
    c=0
    while True:

        if(c==0):
            services()
            speak('Can you please tell me which service do you want??')
            speak('Enter your choice in the input console')
            c=c+1
            n = int(input('Enter here:'))
        else:
            time.sleep(5)


            speak('Press Y to continue service....')
            t = input('Press Y or y to continue service....')
            services()

            if t=='Y' or t=='y':
                n = int(input('Enter your choice:'))
            else:
                exit()


        if n==1:
            print('Loading.........')
            time.sleep(4)
            schedule()
        if n==2:
            print('Loading.........')
            time.sleep(4)
            wiki()
        if n ==3:
            youtube()
        if n==4:
            print('Loading.........')
            time.sleep(4)
            openmeet()
        if n == 5:
            print('Loading.........')
            time.sleep(4)
            sendmail()
            speak('Mail sent.')
            print('mail sent')
        if n == 6:
            print('Loading.........')
            time.sleep(4)
            readdiary()
        if n == 7:
            print('Loading.........')
            time.sleep(4)
            listenmusic()
        if n==8:
            print('Exitting from the system')
            speak('Exitting from the system,Have a nice day ahead sir..')
            notification.notify(
                title='Exitting out systems',
                message="Going Back To Sleep ",
                # app_icon="C:\\Users\\Krishna\\Downloads\\google_assistant_icon-icons.com_61478\.ico",
                # displaying time
                timeout=3
            )
            exit()







