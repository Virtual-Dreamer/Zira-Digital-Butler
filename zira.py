import speech_recognition as sr
import webbrowser as wb
import pyttsx3
import random
import winsound
import cv2
from pygame import *
import sys
import os
import requests
import platform
import wmi
import psutil
from datetime import datetime

mixer.init()
engine = pyttsx3.init()  # initialize pyttsx3 for us to be able to use it
computer = wmi.WMI()

recognizer1 = sr.Recognizer()  # instance of recognizer
recognizer2 = sr.Recognizer()
recognizer3 = sr.Recognizer()


def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


def main():

    window_name = "Zira is recording this!"  # title of window in video recording
    cv2.namedWindow(window_name)

    cap = cv2.VideoCapture(0)

    filename = "C:\\Zira\\Video\\Video.avi"
    codec = cv2.VideoWriter_fourcc("X", "V", "I", "D")
    frame_rate = 30
    resolution = (640, 480)

    video_output = cv2.VideoWriter(filename, codec, frame_rate, resolution)

    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False

    while ret:
        ret, frame = cap.read()

        video_output.write(frame)

        cv2.imshow(window_name, frame)
        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()
    video_output.release()
    cap.release()


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


def take_picture():
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("Selfie with Zira!")

    img_counter = 0

    print("Welcome to Zira's Photobooth!")
    engine.say("Welcome to Zira's Photobooth!")
    engine.runAndWait()
    print("Oh how I love photography.")
    engine.say("Oh how I love photography")
    engine.runAndWait()
    print("Please press the SPACE bar to capture pictures.")
    engine.say("Please press the SPACE bar to capture pictures.")
    engine.runAndWait()
    print("The pictures will be saved to C:\\Zira\\Images. The output file name will be Image.png")
    engine.say("The pictures will be saved to C:\\Zira\\Images. The output file name will be Image.png")
    engine.runAndWait()
    print("Please press the ESCAPE key to quit taking pictures.")
    engine.say("Please press the ESCAPE key to quit taking pictures.")
    engine.runAndWait()

    while True:
        ret, frame = cam.read()
        cv2.imshow("Selfie with Zira!", frame)
        if not ret:
            break
        k = cv2.waitKey(1)

        if k % 256 == 27:
            print("Escape button hit. Shutting down camera...")
            engine.say("Escape button hit. Shutting down camera...")
            engine.runAndWait()
            break
        elif k % 256 == 32:
            print("Say cheese!")
            engine.say("Say cheese!")
            engine.runAndWait()
            img_name = "C:\\Zira\\Images\\Image{}.png".format(img_counter)
            engine.say("{} captured!".format(img_name[15:]))
            engine.runAndWait()
            print("{} captured!".format(img_name[15:]))
            cv2.imwrite(img_name, frame)
            img_counter += 1

    cam.release()

    cv2.destroyAllWindows()


def get_weather(user_city):
    weather_key = "d94549da77adfc618cf89202b6246b03"
    url_weather = "https://api.openweathermap.org/data/2.5/weather"
    params_weather = {"APPID": weather_key, "q": user_city, "units": "Metric"}
    print("Getting weather in", user_city.title())
    engine.say("Getting weather in " + str(user_city))
    engine.runAndWait()
    response_weather = requests.get(url_weather, params=params_weather)
    weather = response_weather.json()  # KAPAG ERROR ANG RESULT NITO. DONT FORGET

    if str(weather["cod"]) == "200":
        print("City: " + str(weather["name"]))
        engine.say("City: " + str(weather["name"]))
        engine.runAndWait()
        print("Country: " + str(weather["sys"]["country"]))
        engine.say("Country: " + str(weather["sys"]["country"]))
        engine.runAndWait()
        print("Weather: " + str(weather["weather"][0]["description"]))
        engine.say("Weather: " + str(weather["weather"][0]["description"]))
        engine.runAndWait()
        print("Temperature in Celsius: " + str(weather["main"]["temp"]))
        engine.say("Temperature in Celsius: " + str(weather["main"]["temp"]))
        engine.runAndWait()

    elif str(weather["cod"]) == "404":
        print("City not found. Please try again.")
        engine.say("City not found. Please try again.")
        engine.runAndWait()


path = "C:\\Zira\\"
if not os.path.exists(path):
    os.makedirs(path)

Video_path = "C:\\Zira\\Video"
if not os.path.exists(Video_path):
    os.makedirs(Video_path)

Image_path = "C:\\Zira\\Images"
if not os.path.exists(Image_path):
    os.makedirs(Image_path)

Music_path = "C:\\Zira\\Music"
if not os.path.exists(Music_path):
    os.makedirs(Music_path)

Place_path = "C:\\Zira\\Place"
if not os.path.exists(Place_path):
    os.makedirs(Place_path)


engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0')
print("Good day, operator! Zira at your service. How can I help you?")
engine.say("Good day, operator! Zira at your service. How can I help you?")
engine.runAndWait()

while True:  # while the program is open, this will execute
    with sr.Microphone() as src:
        print("Zira is listening...")
        audio = recognizer2.listen(src, phrase_time_limit=5)

    try:
        if "duckduckgo" in recognizer1.recognize_google(audio, language="en-US"):
            print("Initializing DuckDuckGo..")
            engine.say("Initializing DuckDuckGo...")
            engine.runAndWait()
            print("DuckDuckGo initialized.")
            engine.say("DuckDuckGo initialized.")
            engine.runAndWait()
            print("What do you need, operator?")
            engine.say("What do you need, operator?")
            engine.runAndWait()

            while True:  # this will happen while duckduckgo is initialized

                with sr.Microphone() as src:
                    print("Search for?")
                    audio = recognizer1.listen(src, phrase_time_limit=5)

                    try:

                        if "facebook" in recognizer1.recognize_google(audio, language="en-US"):
                            get = recognizer1.recognize_google(audio)
                            url = "https://www.facebook.com"
                            print("You said: ", get)
                            print("Opening facebook. Please wait a little while, operator.")
                            engine.say("Opening facebook. Please wait a little while, operator")
                            engine.runAndWait()
                            wb.get().open_new(url)
                            print("Done opening facebook.")
                            engine.say("Done opening facebook")
                            engine.runAndWait()

                        elif "youtube" in recognizer1.recognize_google(audio, language="en-US"):
                            get = recognizer1.recognize_google(audio)
                            url = "https://www.youtube.com"
                            print("You said: ", get)
                            print("Opening youtube.")
                            engine.say("Opening youtube.")
                            engine.runAndWait()
                            wb.get().open_new(url)
                            print("Done opening youtube.")
                            engine.say("Done opening youtube")
                            engine.runAndWait()

                        elif "twitter" in recognizer1.recognize_google(audio, language="en-US"):
                            get = recognizer1.recognize_google(audio)
                            url = "https://www.twitter.com"
                            print("You said: ", get)
                            print("Opening Twitter...")
                            engine.say("Opening twitter")
                            engine.runAndWait()
                            wb.get().open_new(url)
                            print("Done opening Twitter.")
                            engine.say("Done opening twitter")
                            engine.runAndWait()

                        elif "instagram" in recognizer1.recognize_google(audio, language="en-US"):
                            get = recognizer1.recognize_google(audio)
                            url = "https://www.instagram.com"
                            print("You said: ", get)
                            print("Opening Instagram...")
                            engine.say("Opening instagram")
                            engine.runAndWait()
                            wb.get().open_new(url)
                            print("Done opening Instagram.")
                            engine.say("Done opening instagram")
                            engine.runAndWait()

                        elif "pass" in recognizer1.recognize_google(audio, language="en-US"):
                            print("Shutting down DuckDuckGo...")
                            engine.say("Shutting down DuckDuckGo")
                            engine.runAndWait()
                            print("DuckDuckGo shut down.")
                            engine.say("DuckDuckGo shut down")
                            engine.runAndWait()
                            break

                        elif "are you there" in recognizer1.recognize_google(audio, language="en-US"):
                            print("I'm here, operator.")
                            engine.say("I'm here, operator")
                            engine.runAndWait()

                        elif "shutdown" in recognizer1.recognize_google(audio, language="en-US"):
                            print("Shutting down...")
                            engine.say("Shutting down...")
                            engine.runAndWait()
                            exit()

                        else:
                            url = "https://duckduckgo.com/?q="
                            get = recognizer1.recognize_google(audio)
                            print("You said: ", get)
                            print("Searching for " + str(get))
                            engine.say("Searching for" + str(get))
                            engine.runAndWait()
                            wb.get().open_new(url + get)

                    except sr.UnknownValueError:
                        engine.say(" ")
                        engine.runAndWait()

                    except sr.RequestError as e:
                        engine.say(" ")
                        engine.runAndWait()

     
        # APPLICATIONS

        elif "simple notepad" in recognizer1.recognize_google(audio, language="en-US"):
            print("Now opening Notepad...")
            engine.say("Now opening notepad")
            engine.runAndWait()
            os.startfile("C:\\Windows\\System32\\notepad.exe")
            print("Done opening Notepad")
            engine.say("Done opening notepad")
            engine.runAndWait()
            print("Standby for your commands...")
            engine.say("Standby for your commands")
            engine.runAndWait()

            while True:  # while notepad is open, you can use the commands in TRY:
                with sr.Microphone() as src:
                    recognizer3 = sr.Recognizer()
                    audio1 = recognizer3.listen(src, timeout=1, phrase_time_limit=5)

                try:
                    if "close" in recognizer3.recognize_google(audio1, language='en-US'):
                        print("Shutting down Notepad...")
                        engine.say("Shutting down notepad")
                        engine.runAndWait()
                        os.system("TASKKILL /F /IM notepad.exe")
                        print("Notepad shut down.")
                        engine.say("Notepad shut down")
                        engine.runAndWait()
                        break

                    elif "pass" in recognizer3.recognize_google(audio1, language="en-US"):
                        print("Leaving Notepad in your hands, operator.")
                        engine.say("Leaving notepad in your hands, operator")
                        engine.runAndWait()
                        break

                    elif "are you there" in recognizer3.recognize_google(audio1, language="en-US"):
                        print("I'm here, operator.")
                        engine.say("I'm here, operator")
                        engine.runAndWait()

                except sr.WaitTimeoutError:
                    engine.say(" ")
                    engine.runAndWait()

                except sr.UnknownValueError:
                    engine.say(" ")
                    engine.runAndWait()

                except sr.RequestError:
                    engine.say("Could not request result. Please try again")
                    engine.runAndWait()

        elif "notepad plus plus" in recognizer1.recognize_google(audio, language="en-US"):
            print("Now opening Notepad++")
            engine.say("Now opening notepad++")
            engine.runAndWait()
            os.startfile("C:\\Program Files\\Notepad++\\notepad++.exe")
            print("Done opening Notepad++")
            engine.say("Done opening notepad++")
            engine.runAndWait()
            print("Standby for your commands...")
            engine.say("Standby for your commands")
            engine.runAndWait()

            while True:
                with sr.Microphone() as src:
                    recognizer3 = sr.Recognizer()
                    audio1 = recognizer3.listen(src, timeout=1, phrase_time_limit=5)

                try:
                    if "close" in recognizer3.recognize_google(audio1, language='en-US'):
                        print("Shutting down Notepad++...")
                        engine.say("Shutting down notepad++")
                        engine.runAndWait()
                        os.system("TASKKILL /F /IM notepad++.exe")
                        print("Notepad++ shut down")
                        engine.say("Notepad++ shut down")
                        engine.runAndWait()
                        break

                    elif "pass" in recognizer3.recognize_google(audio1, language="en-US"):
                        print("Leaving Notepad++ in your hands, operator.")
                        engine.say("Leaving notepad++ in your hands, operator")
                        engine.runAndWait()
                        break

                    elif "are you there" in recognizer3.recognize_google(audio1, language="en-US"):
                        print("I'm here, operator.")
                        engine.say("I'm here, operator")
                        engine.runAndWait()

                except sr.WaitTimeoutError:
                    engine.say(" ")
                    engine.runAndWait()

                except sr.UnknownValueError:
                    engine.say(" ")
                    engine.runAndWait()

                except sr.RequestError:
                    engine.say("Could not request result. Please try again")
                    engine.runAndWait()

        elif "paint" in recognizer1.recognize_google(audio, language="en-US"):
            print("Now opening Paint...")
            engine.say("Now opening paint")
            engine.runAndWait()
            os.startfile("C:\\WINDOWS\\system32\\mspaint.exe")
            print("Done opening Paint.")
            engine.say("Done opening paint")
            engine.runAndWait()
            print("Standby for your commands...")
            engine.say("Standby for your commands")
            engine.runAndWait()

            while True:
                with sr.Microphone() as src:
                    recognizer3 = sr.Recognizer()
                    audio1 = recognizer3.listen(src, timeout=1, phrase_time_limit=5)

                try:
                    if "close" in recognizer3.recognize_google(audio1, language='en-US'):
                        print("Shutting down Paint...")
                        engine.say("Shutting down paint")
                        engine.runAndWait()
                        os.system("TASKKILL /F /IM mspaint.exe")
                        print("Paint shut down.")
                        engine.say("Paint shut down")
                        engine.runAndWait()
                        break

                    elif "pass" in recognizer3.recognize_google(audio1, language="en-US"):
                        print("Leaving paint in your hands, operator.")
                        engine.say("Leaving paint in your hands, operator")
                        engine.runAndWait()
                        break

                    elif "are you there" in recognizer3.recognize_google(audio1, language="en-US"):
                        print("I'm here, operator.")
                        engine.say("I'm here, operator")
                        engine.runAndWait()

                except sr.WaitTimeoutError:
                    engine.say(" ")
                    engine.runAndWait()

                except sr.UnknownValueError:
                    engine.say(" ")
                    engine.runAndWait()

                except sr.RequestError:
                    engine.say("Could not request result. Please try again")
                    engine.runAndWait()

        elif "powerpoint" in recognizer1.recognize_google(audio, language='en-US'):
            print("Now opening Microsoft Powerpoint...")
            engine.say("Now opening Microsoft Powerpoint")
            engine.runAndWait()
            os.startfile("C:\\Program Files\\Microsoft Office\\Office15\\POWERPNT.exe")
            print("Done opening Microsoft Powerpoint")
            engine.say("Done opening Microsoft Powerpoint")
            engine.runAndWait()
            print("Standby for your commands...")
            engine.say("Standby for your commands")
            engine.runAndWait()

            while True:
                with sr.Microphone() as src:
                    recognizer3 = sr.Recognizer()
                    audio2 = recognizer3.listen(src, timeout=1, phrase_time_limit=5)

                try:
                    if "close" in recognizer3.recognize_google(audio2, language="en-US"):
                        print("Shutting down Microsoft Powerpoint")
                        engine.say("Shutting down Microsoft Powerpoint.")
                        engine.runAndWait()
                        os.system("TASKKILL /F /IM POWERPNT.exe")
                        print("Microsoft Powerpoint shut down.")
                        engine.say("Microsoft powerpoint shut down.")
                        engine.runAndWait()
                        break

                    elif "pass" in recognizer3.recognize_google(audio2, language="en-US"):
                        print("Leaving Powerpoint in your hands, operator.")
                        engine.say("Leaving powerpoint in your hands, operator.")
                        engine.runAndWait()
                        break

                    elif "are you there" in recognizer3.recognize_google(audio2, language="en-US"):
                        print("I'm here, operator.")
                        engine.say("I'm here, operator.")
                        engine.runAndWait()

                except sr.UnknownValueError:
                    engine.say(" ")
                    engine.runAndWait()

                except sr.RequestError:
                    engine.say(" ")
                    engine.runAndWait()

        elif "word" in recognizer1.recognize_google(audio, language='en-US'):
            print("Now opening Microsoft Word...")
            engine.say("Now opening Microsoft Word")
            engine.runAndWait()
            os.startfile("C:\\Program Files\\Microsoft Office\\Office15\\WINWORD.exe")
            print("Done opening Microsoft Word.")
            engine.say("Done opening Microsoft Word")
            engine.runAndWait()
            print("Standby for your commands...")
            engine.say("Standby for your commands")
            engine.runAndWait()

            while True:
                with sr.Microphone() as src:
                    recognizer3 = sr.Recognizer()
                    audio3 = recognizer3.listen(src, timeout=1, phrase_time_limit=5)

                try:
                    if "close" in recognizer3.recognize_google(audio3, language="en-US"):
                        print("Shutting down Microsoft Word...")
                        engine.say("Shutting down Microsoft Word")
                        engine.runAndWait()
                        os.system("TASKKILL /F /IM WINWORD.exe")
                        print("Microsoft Word shut down")
                        engine.say("Microsoft Word shut down")
                        engine.runAndWait()
                        break

                    elif "pass" in recognizer3.recognize_google(audio3, language="en-US"):
                        print("Leaving Word in your hands, operator.")
                        engine.say("Leaving word in your hands, operator")
                        engine.runAndWait()
                        break

                    elif "are you there" in recognizer3.recognize_google(audio3, language="en-US"):
                        print("I'm here, operator.")
                        engine.say("I'm here, operator")
                        engine.runAndWait()

                except sr.UnknownValueError:
                    engine.say(" ")
                    engine.runAndWait()

                except sr.RequestError:
                    engine.say(" ")
                    engine.runAndWait()

        elif "excel" in recognizer1.recognize_google(audio, language='en-US'):
            print("Now opening Microsoft Excel...")
            engine.say("Now opening Microsoft Excel")
            os.startfile("C:\\Program Files\\Microsoft Office\\Office15\\EXCEL.exe")
            print("Done opening Microsoft Excel.")
            engine.say("Done opening Microsoft Excel")
            print("Standby for your commands...")
            engine.say("Standby for your commands")
            engine.runAndWait()

            while True:
                with sr.Microphone() as src:
                    recognizer3 = sr.Recognizer()
                    audio4 = recognizer3.listen(src, timeout=1, phrase_time_limit=5)

                try:
                    if "close" in recognizer3.recognize_google(audio4, language="en-US"):
                        print("Shutting down Microsoft Excel...")
                        engine.say("Shutting down Microsoft Excel")
                        os.system("TASKKILL /F /IM EXCEL.exe")
                        print("Microsoft Excel shut down.")
                        engine.say("Microsoft Excel shut down")
                        engine.runAndWait()
                        break

                    elif "pass" in recognizer3.recognize_google(audio4, language="en-US"):
                        print("Leaving Excel in your hands, operator.")
                        engine.say("Leaving excel in your hands, operator")
                        engine.runAndWait()
                        break

                    elif "are you there" in recognizer3.recognize_google(audio4, language="en-US"):
                        print("I'm here, operator.")
                        engine.say("I'm here, operator")
                        engine.runAndWait()

                except sr.UnknownValueError:
                    engine.say(" ")
                    engine.runAndWait()

                except sr.RequestError:
                    engine.say(" ")
                    engine.runAndWait()

        elif "get weather" in recognizer1.recognize_google(audio, language="en-US"):
            print("Please specify the city.")
            engine.say("Please specify the city.")
            engine.runAndWait()

            while True:
                with sr.Microphone() as src:
                    audio7 = recognizer1.listen(src, timeout=1, phrase_time_limit=5)
                    city = recognizer2.recognize_google(audio7)

                    get_weather(city)
                    break

        elif "system information" in recognizer1.recognize_google(audio, language="en-US"):
            computer_info = computer.Win32_ComputerSystem()[0]
            os_info = computer.Win32_OperatingSystem()[0]
            proc_info = computer.Win32_Processor()[0]
            gpu_info = computer.Win32_VideoController()[0]

            partitions = psutil.disk_partitions()

            os_name = os_info.Name.encode('utf-8').split(b'|')[0]
            os_version = ' '.join([os_info.Version, os_info.BuildNumber])
            system_ram = float(os_info.TotalVisibleMemorySize) / 1048576  # KB to GB

            print("Now reading my system information...")
            engine.say("Now reading my system information....")
            engine.runAndWait()
            print("My operating system is {0}".format(os_name).replace("b", "").replace("'", ""))
            engine.say(str("My operating system is {0}".format(os_name).replace("b", "").replace("'", "")))
            engine.runAndWait()
            print("I'm using version {0}".format(os_version[0:9]))
            engine.say(str("I'm using version {0}".format(os_version[0:9])))
            engine.runAndWait()
            print('My processor is {0}'.format(proc_info.Name))
            engine.say(str('My processor is {0}'.format(proc_info.Name)))
            engine.runAndWait()
            print('I have a memory of {0} GB'.format('%.2f' % system_ram))
            engine.say(str('I have a memory of {0} GB'.format('%.2f' % system_ram)))
            engine.runAndWait()
            print('My graphics card is {0}'.format(gpu_info.Name))
            engine.say(str('My graphics card is {0}'.format(gpu_info.Name)))
            engine.runAndWait()
            print("My alias is", platform.node())
            engine.say(str("My alias is " + platform.node()))
            engine.runAndWait()
            for partition in partitions:
                print("My " + str(partition.device).replace("\\", "") + " drive is active.")
                engine.say("My " + str(partition.device).replace("\\", "") + " drive is active.")
                engine.runAndWait()
                if str(partition.fstype) == "":
                    print("No file system detected.")
                    engine.say("No file system detected.")
                    engine.runAndWait()
                else:
                    print("Its file system is " + str(partition.fstype) + ".")
                    engine.say("Its file system is " + str(partition.fstype) + ".")
                    engine.runAndWait()
                try:
                    partition_usage = psutil.disk_usage(partition.mountpoint)
                except PermissionError:
                    continue

                print("Its total size is " + str(get_size(partition_usage.total)) + ".")
                engine.say("Its total size is " + str(get_size(partition_usage.total)) + ".")
                engine.runAndWait()
                print(str(get_size(partition_usage.used) + " is currently used in this drive."))
                engine.say(str(get_size(partition_usage.used) + " is currently used in this drive."))
                engine.runAndWait()
                print("There's currently " + str(get_size(partition_usage.free) + " free space in this drive."))
                engine.say("There's currently " + str(get_size(partition_usage.free) + " free space in this drive."))
                engine.runAndWait()

        elif "status" in recognizer1.recognize_google(audio, language="en-US"):
            bat = psutil.sensors_battery()
            print("Now reading system status...")
            engine.say("Now reading system status...")
            engine.runAndWait()
            print("My battery is currently on", str(bat[0]), "%")
            engine.say("My battery is currently on" + str(bat[0]) + "%")
            engine.runAndWait()
            if str(bat[2]) == "False":
                print("I am not charging.")
                engine.say("I am not charging.")
                print("Estimating", bat[1], "seconds left before shutdown")
                engine.say("Estimating" + str(bat[1]) + "seconds left before shutdown")
                engine.runAndWait()
                engine.runAndWait()
            else:
                print("I'm currently charging.")
                engine.say("I'm currently charging.")
                engine.runAndWait()

        elif "wake up" in recognizer1.recognize_google(audio, language="en-US"):
            boot_time = psutil.boot_time()
            bt = datetime.fromtimestamp(boot_time)
            print(f"I woke up in {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")
            engine.say(str(f"I woke up in {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}"))
            engine.runAndWait()

        elif "text message" in recognizer1.recognize_google(audio, language="en-US"):
            print("Initializing Messaging System...")
            engine.say("Initializing Messaging System...")
            engine.runAndWait()
            print("Messaging System initialized!")
            engine.say("Messaging System initialized!")
            engine.runAndWait()

            while True:
                try:
                    print("What is the phone number of the recipient?")
                    engine.say("What is the phone number of the recipient?")
                    engine.runAndWait()

                    with sr.Microphone() as src:
                        mobile = recognizer1.listen(src, timeout=1, phrase_time_limit=10)
                        phone = recognizer1.recognize_google(mobile, language="en-US")
                        if "exit" in phone:
                            print("Messaging System shutting down...")
                            engine.say("Messaging System shutting down...")
                            engine.runAndWait()
                            break
                        else:
                            print("The phone number is: " + str(phone).replace(" ", ""))
                            engine.say("The phone number is: " + str(phone).replace(" ", ""))
                            engine.runAndWait()

                        print("Is this correct?")
                        engine.say("Is this correct?")
                        engine.runAndWait()

                        with sr.Microphone() as src1:
                            auth = recognizer1.listen(src1, timeout=1, phrase_time_limit=5)
                            auth1 = recognizer1.recognize_google(auth, language="en-US")

                            while True:

                                if "yes" in recognizer1.recognize_google(auth, language="en-US"):
                                    print("What is your message?")
                                    engine.say("What is your message?")
                                    engine.runAndWait()

                                    with sr.Microphone() as src2:
                                        message = recognizer1.listen(src2, timeout=1, phrase_time_limit=20)
                                        msg = recognizer1.recognize_google(message, language="en-US")
                                        print("Your message is: " + str(msg))
                                        engine.say("Your message is: " + str(msg))
                                        engine.runAndWait()

                                        url = "https://api.botscripts.net/mensahe/"
                                        params = {"phone": str(phone).replace(" ", ""), "message": str(msg)}
                                        r = requests.post(url, params)

                                        if str(r.status_code) == "200":
                                            print("Message sent successfully!")
                                            engine.say("Message sent successfully!")
                                            engine.runAndWait()
                                            break
                                        elif str([r.status_code]) == "500":
                                            print("Invalid request.")
                                            engine.say("Invalid request.")
                                            engine.runAndWait()
                                        elif str(r.status_code) == "501":
                                            print("Phone number is invalid.")
                                            engine.say("Phone number is invalid.")
                                            engine.runAndWait()
                                        elif str(r.status_code) == "502":
                                            print("Message is too short. "
                                                  "The message to be sent must not be less than"
                                                  " 10 and greater than 160 characters.")
                                            engine.say("Message is too short. "
                                                       "The message to be sent must not be less than "
                                                       "10 and greater than 160 characters.")
                                            engine.runAndWait()
                                        elif str(result["status"]) == "503":
                                            print("Message is too long. "
                                                  "The message to be sent must not be less than 10 "
                                                  "and greater than 160 characters.")
                                            engine.say("Message is too long. "
                                                       "The message to be sent must not be less than 10"
                                                       " and greater than 160 characters.")
                                            engine.runAndWait()
                                        elif str(result["status"]) == "507":
                                            print("Queue wait timer. "
                                                  "30 minutes is the waiting time"
                                                  " to send another message to the same number.")
                                            engine.say("Queue wait timer."
                                                       " 30 minutes is the waiting time "
                                                       "to send another message to the same number.")
                                            engine.runAndWait()
                                            break

                                elif "no" in recognizer1.recognize_google(auth, language="en-US"):
                                    break

                except sr.WaitTimeoutError:
                    print("Something happened. Please try again.")
                    engine.say("Something happened. Please try again.")
                    engine.runAndWait()

                except sr.RequestError:
                    print("Unstable internet connection. Please try again.")
                    engine.say("Unstable internet connection. Please try again.")
                    engine.runAndWait()

                except sr.UnknownValueError:
                    print("Voice unrecognizable. Please try again.")
                    engine.say("Voice unrecognizable. Please try again.")
                    engine.runAndWait()

        if "search a place" in recognizer1.recognize_google(audio, language="en-US"):
            link = "http://www.mapquestapi.com/geocoding/v1/address"
            key = "cx0ZbCBVqAKNpYkVi2nUejGOE6mzhSWl"

            print("Initializing Zira's Place Searching system...")
            engine.say("Initializing Zira's Place Searching system...")
            engine.runAndWait()
            print("Place Searching system initialized!")
            engine.say("Place Searching system initialized!")
            engine.runAndWait()
            print("What are you looking for, operator?")
            engine.say("What are you looking for, operator?")
            engine.runAndWait()

            while True:
                with sr.Microphone() as src:
                    audio9 = recognizer1.listen(src, timeout=1, phrase_time_limit=5)
                    place = recognizer1.recognize_google(audio9, language="en-US")
                    break

            print("Where do you want me to look for " + str(place).title() + "?")
            engine.say("Where do you want me to look for " + str(place).title() + "?")
            engine.runAndWait()

            while True:
                with sr.Microphone() as src:
                    audio8 = recognizer1.listen(src, timeout=1, phrase_time_limit=5)
                    geocode = recognizer1.recognize_google(audio8, language="en-US")

                try:
                    location = str(geocode)
                    params = {"key": key, "location": location}
                    response = requests.get(link, params=params)
                    result = response.json()
                    lot_lang = str(result["results"][0]["locations"][0]["latLng"]).replace("{", "").replace("}", "")\
                        .replace("'", "").replace("lat", "").replace("lng", "").replace(":", "").replace(" ", "")

                    url = "https://places.cit.api.here.com/places/v1/autosuggest"
                    app_id = "XuNdxJoB4cfZ1DZSQzga"
                    app_code = "yINTzro-1a5Gsf_7GEpZfA"
                    at = lot_lang
                    q = place

                    params = {"app_id": app_id, "app_code": app_code, "at": at, "q": q}
                    response = requests.get(url, params=params)
                    output = response.json()

                    print("Now searching for " + str(place).title() + " in " + str(result["results"][0]["providedLocation"]["location"]).title() + "...")
                    engine.say("Now searching for " + str(place).title() + " in " + str(result["results"][0]["providedLocation"]["location"]).title() + "...")
                    engine.runAndWait()

                    print("Category: " + str(output["results"][0]["categoryTitle"]))
                    print("Title: " + str(output["results"][0]["title"]))
                    print("Vicinity: " + str(output["results"][0]["vicinity"]).replace("<br/>", ""))
                    print("Result type: " + str(output["results"][0]["resultType"] + "\n"))

                    print("Category: " + str(output["results"][1]["categoryTitle"]))
                    print("Title: " + str(output["results"][1]["title"]))
                    print("Vicinity: " + str(output["results"][1]["vicinity"]).replace("<br/>", ""))
                    print("Result type: " + str(output["results"][1]["resultType"] + "\n"))

                    print("Category: " + str(output["results"][2]["categoryTitle"]))
                    print("Title: " + str(output["results"][2]["title"]))
                    print("Vicinity: " + str(output["results"][2]["vicinity"]).replace("<br/>", ""))
                    print("Result type: " + str(output["results"][2]["resultType"] + "\n"))

                    print("Category: " + str(output["results"][3]["categoryTitle"]))
                    print("Title: " + str(output["results"][3]["title"]))
                    print("Vicinity: " + str(output["results"][3]["vicinity"]).replace("<br/>", ""))
                    print("Result type: " + str(output["results"][3]["resultType"] + "\n"))

                    print("Category: " + str(output["results"][4]["categoryTitle"]))
                    print("Title: " + str(output["results"][4]["title"]))
                    print("Vicinity: " + str(output["results"][4]["vicinity"]).replace("<br/>", ""))
                    print("Result type: " + str(output["results"][4]["resultType"] + "\n"))

                    print("Category: " + str(output["results"][5]["categoryTitle"]))
                    print("Title: " + str(output["results"][5]["title"]))
                    print("Vicinity: " + str(output["results"][5]["vicinity"]).replace("<br/>", ""))
                    print("Result type: " + str(output["results"][5]["resultType"] + "\n"))

                    print("Category: " + str(output["results"][6]["categoryTitle"]))
                    print("Title: " + str(output["results"][6]["title"]))
                    print("Vicinity: " + str(output["results"][6]["vicinity"]).replace("<br/>", ""))
                    print("Result type: " + str(output["results"][6]["resultType"] + "\n"))

                    print("Category: " + str(output["results"][7]["categoryTitle"]))
                    print("Title: " + str(output["results"][7]["title"]))
                    print("Vicinity: " + str(output["results"][7]["vicinity"]).replace("<br/>", ""))
                    print("Result type: " + str(output["results"][7]["resultType"] + "\n"))

                    print("Category: " + str(output["results"][8]["categoryTitle"]))
                    print("Title: " + str(output["results"][8]["title"]))
                    print("Vicinity: " + str(output["results"][8]["vicinity"]).replace("<br/>", ""))
                    print("Result type: " + str(output["results"][8]["resultType"] + "\n"))

                    print("Category: " + str(output["results"][9]["categoryTitle"]))
                    print("Title: " + str(output["results"][9]["title"]))
                    print("Vicinity: " + str(output["results"][9]["vicinity"]).replace("<br/>", ""))
                    print("Result type: " + str(output["results"][9]["resultType"] + "\n"))

                    print("Category: " + str(output["results"][10]["categoryTitle"]))
                    print("Title: " + str(output["results"][10]["title"]))
                    print("Vicinity: " + str(output["results"][10]["vicinity"]).replace("<br/>", ""))
                    print("Result type: " + str(output["results"][10]["resultType"] + "\n"))

                    print("Category: " + str(output["results"][11]["categoryTitle"]))
                    print("Title: " + str(output["results"][11]["title"]))
                    print("Vicinity: " + str(output["results"][11]["vicinity"]).replace("<br/>", ""))
                    print("Result type: " + str(output["results"][11]["resultType"] + "\n"))

                    print("Category: " + str(output["results"][12]["categoryTitle"]))
                    print("Title: " + str(output["results"][12]["title"]))
                    print("Vicinity: " + str(output["results"][12]["vicinity"]).replace("<br/>", ""))
                    print("Result type: " + str(output["results"][12]["resultType"] + "\n"))

                    print("Category: " + str(output["results"][13]["categoryTitle"]))
                    print("Title: " + str(output["results"][13]["title"]))
                    print("Vicinity: " + str(output["results"][13]["vicinity"]).replace("<br/>", ""))
                    print("Result type: " + str(output["results"][13]["resultType"] + "\n"))

                    print("Category: " + str(output["results"][14]["categoryTitle"]))
                    print("Title: " + str(output["results"][14]["title"]))
                    print("Vicinity: " + str(output["results"][14]["vicinity"]).replace("<br/>", ""))
                    print("Result type: " + str(output["results"][14]["resultType"] + "\n"))

                    print("Category: " + str(output["results"][15]["categoryTitle"]))
                    print("Title: " + str(output["results"][15]["title"]))
                    print("Vicinity: " + str(output["results"][15]["vicinity"]).replace("<br/>", ""))
                    print("Result type: " + str(output["results"][15]["resultType"] + "\n"))

                    print("Category: " + str(output["results"][16]["categoryTitle"]))
                    print("Title: " + str(output["results"][16]["title"]))
                    print("Vicinity: " + str(output["results"][16]["vicinity"]).replace("<br/>", ""))
                    print("Result type: " + str(output["results"][16]["resultType"] + "\n"))

                    print("Category: " + str(output["results"][17]["categoryTitle"]))
                    print("Title: " + str(output["results"][17]["title"]))
                    print("Vicinity: " + str(output["results"][17]["vicinity"]).replace("<br/>", ""))
                    print("Result type: " + str(output["results"][17]["resultType"] + "\n"))

                    print("Category: " + str(output["results"][18]["categoryTitle"]))
                    print("Title: " + str(output["results"][18]["title"]))
                    print("Vicinity: " + str(output["results"][18]["vicinity"]).replace("<br/>", ""))
                    print("Result type: " + str(output["results"][18]["resultType"] + "\n"))

                    print("Category: " + str(output["results"][19]["categoryTitle"]))
                    print("Title: " + str(output["results"][19]["title"]))
                    print("Vicinity: " + str(output["results"][19]["vicinity"]).replace("<br/>", ""))
                    print("Result type: " + str(output["results"][19]["resultType"] + "\n"))

                    print("Do you want to save the output, operator?")
                    engine.say("Do you want to save the output, operator?")
                    engine.runAndWait()

                    with sr.Microphone() as src:
                        audio10 = recognizer1.listen(src, timeout=1, phrase_time_limit=5)

                        while True:

                            if "yes" in recognizer1.recognize_google(audio10, language="en-US"):
                                print("Saving the output to a text file...")
                                engine.say("Saving the output to a text file...")
                                engine.runAndWait()

                                with open("C:\\Zira\\Place\\Output.txt", "w") as result_file:
                                    result_file.write(
                                        "Category: {0}".format(str(output["results"][0]["categoryTitle"] + "\n")))
                                    result_file.write("Title: {0}".format(str(output["results"][0]["title"] + "\n")))
                                    result_file.write("Vicinity: {0}".format(
                                        str(output["results"][0]["vicinity"]).replace("<br/>", "") + "\n"))
                                    result_file.write(
                                        "Result type: {0}".format(str(output["results"][0]["resultType"] + "\n")))
                                    result_file.write("\n")
                                    result_file.write(
                                        "Category: {0}".format(str(output["results"][1]["categoryTitle"] + "\n")))
                                    result_file.write("Title: {0}".format(str(output["results"][1]["title"] + "\n")))
                                    result_file.write("Vicinity: {0}".format(
                                        str(output["results"][1]["vicinity"]).replace("<br/>", "") + "\n"))
                                    result_file.write(
                                        "Result type: {0}".format(str(output["results"][1]["resultType"] + "\n")))
                                    result_file.write("\n")
                                    result_file.write(
                                        "Category: {0}".format(str(output["results"][2]["categoryTitle"] + "\n")))
                                    result_file.write("Title: {0}".format(str(output["results"][2]["title"] + "\n")))
                                    result_file.write("Vicinity: {0}".format(
                                        str(output["results"][2]["vicinity"]).replace("<br/>", "") + "\n"))
                                    result_file.write(
                                        "Result type: {0}".format(str(output["results"][2]["resultType"] + "\n")))
                                    result_file.write("\n")
                                    result_file.write(
                                        "Category: {0}".format(str(output["results"][3]["categoryTitle"] + "\n")))
                                    result_file.write("Title: {0}".format(str(output["results"][3]["title"] + "\n")))
                                    result_file.write("Vicinity: {0}".format(
                                        str(output["results"][3]["vicinity"]).replace("<br/>", "") + "\n"))
                                    result_file.write(
                                        "Result type: {0}".format(str(output["results"][3]["resultType"] + "\n")))
                                    result_file.write("\n")
                                    result_file.write(
                                        "Category: {0}".format(str(output["results"][4]["categoryTitle"] + "\n")))
                                    result_file.write("Title: {0}".format(str(output["results"][4]["title"] + "\n")))
                                    result_file.write("Vicinity: {0}".format(
                                        str(output["results"][4]["vicinity"]).replace("<br/>", "") + "\n"))
                                    result_file.write(
                                        "Result type: {0}".format(str(output["results"][4]["resultType"] + "\n")))
                                    result_file.write("\n")
                                    result_file.write(
                                        "Category: {0}".format(str(output["results"][5]["categoryTitle"] + "\n")))
                                    result_file.write("Title: {0}".format(str(output["results"][5]["title"] + "\n")))
                                    result_file.write("Vicinity: {0}".format(
                                        str(output["results"][5]["vicinity"]).replace("<br/>", "") + "\n"))
                                    result_file.write(
                                        "Result type: {0}".format(str(output["results"][5]["resultType"] + "\n")))
                                    result_file.write("\n")
                                    result_file.write(
                                        "Category: {0}".format(str(output["results"][6]["categoryTitle"] + "\n")))
                                    result_file.write("Title: {0}".format(str(output["results"][6]["title"] + "\n")))
                                    result_file.write("Vicinity: {0}".format(
                                        str(output["results"][6]["vicinity"]).replace("<br/>", "") + "\n"))
                                    result_file.write(
                                        "Result type: {0}".format(str(output["results"][6]["resultType"] + "\n")))
                                    result_file.write("\n")
                                    result_file.write(
                                        "Category: {0}".format(str(output["results"][7]["categoryTitle"] + "\n")))
                                    result_file.write("Title: {0}".format(str(output["results"][7]["title"] + "\n")))
                                    result_file.write("Vicinity: {0}".format(
                                        str(output["results"][7]["vicinity"]).replace("<br/>", "") + "\n"))
                                    result_file.write(
                                        "Result type: {0}".format(str(output["results"][7]["resultType"] + "\n")))
                                    result_file.write("\n")
                                    result_file.write(
                                        "Category: {0}".format(str(output["results"][8]["categoryTitle"] + "\n")))
                                    result_file.write("Title: {0}".format(str(output["results"][8]["title"] + "\n")))
                                    result_file.write("Vicinity: {0}".format(
                                        str(output["results"][8]["vicinity"]).replace("<br/>", "") + "\n"))
                                    result_file.write(
                                        "Result type: {0}".format(str(output["results"][8]["resultType"] + "\n")))
                                    result_file.write("\n")
                                    result_file.write(
                                        "Category: {0}".format(str(output["results"][9]["categoryTitle"] + "\n")))
                                    result_file.write("Title: {0}".format(str(output["results"][9]["title"] + "\n")))
                                    result_file.write("Vicinity: {0}".format(
                                        str(output["results"][9]["vicinity"]).replace("<br/>", "") + "\n"))
                                    result_file.write(
                                        "Result type: {0}".format(str(output["results"][9]["resultType"] + "\n")))
                                    result_file.write("\n")
                                    result_file.write(
                                        "Category: {0}".format(str(output["results"][10]["categoryTitle"] + "\n")))
                                    result_file.write("Title: {0}".format(str(output["results"][10]["title"] + "\n")))
                                    result_file.write("Vicinity: {0}".format(
                                        str(output["results"][10]["vicinity"]).replace("<br/>", "") + "\n"))
                                    result_file.write(
                                        "Result type: {0}".format(str(output["results"][10]["resultType"] + "\n")))
                                    result_file.write("\n")
                                    result_file.write(
                                        "Category: {0}".format(str(output["results"][11]["categoryTitle"] + "\n")))
                                    result_file.write("Title: {0}".format(str(output["results"][11]["title"] + "\n")))
                                    result_file.write("Vicinity: {0}".format(
                                        str(output["results"][11]["vicinity"]).replace("<br/>", "") + "\n"))
                                    result_file.write(
                                        "Result type: {0}".format(str(output["results"][11]["resultType"] + "\n")))
                                    result_file.write("\n")
                                    result_file.write(
                                        "Category: {0}".format(str(output["results"][12]["categoryTitle"] + "\n")))
                                    result_file.write("Title: {0}".format(str(output["results"][12]["title"] + "\n")))
                                    result_file.write("Vicinity: {0}".format(
                                        str(output["results"][12]["vicinity"]).replace("<br/>", "") + "\n"))
                                    result_file.write(
                                        "Result type: {0}".format(str(output["results"][12]["resultType"] + "\n")))
                                    result_file.write("\n")
                                    result_file.write(
                                        "Category: {0}".format(str(output["results"][13]["categoryTitle"] + "\n")))
                                    result_file.write("Title: {0}".format(str(output["results"][13]["title"] + "\n")))
                                    result_file.write("Vicinity: {0}".format(
                                        str(output["results"][13]["vicinity"]).replace("<br/>", "") + "\n"))
                                    result_file.write(
                                        "Result type: {0}".format(str(output["results"][13]["resultType"] + "\n")))
                                    result_file.write("\n")
                                    result_file.write(
                                        "Category: {0}".format(str(output["results"][14]["categoryTitle"] + "\n")))
                                    result_file.write("Title: {0}".format(str(output["results"][14]["title"] + "\n")))
                                    result_file.write("Vicinity: {0}".format(
                                        str(output["results"][14]["vicinity"]).replace("<br/>", "") + "\n"))
                                    result_file.write(
                                        "Result type: {0}".format(str(output["results"][14]["resultType"] + "\n")))
                                    result_file.write("\n")
                                    result_file.write(
                                        "Category: {0}".format(str(output["results"][15]["categoryTitle"] + "\n")))
                                    result_file.write("Title: {0}".format(str(output["results"][15]["title"] + "\n")))
                                    result_file.write("Vicinity: {0}".format(
                                        str(output["results"][15]["vicinity"]).replace("<br/>", "") + "\n"))
                                    result_file.write(
                                        "Result type: {0}".format(str(output["results"][15]["resultType"] + "\n")))
                                    result_file.write("\n")
                                    result_file.write(
                                        "Category: {0}".format(str(output["results"][16]["categoryTitle"] + "\n")))
                                    result_file.write("Title: {0}".format(str(output["results"][16]["title"] + "\n")))
                                    result_file.write("Vicinity: {0}".format(
                                        str(output["results"][16]["vicinity"]).replace("<br/>", "") + "\n"))
                                    result_file.write(
                                        "Result type: {0}".format(str(output["results"][16]["resultType"] + "\n")))
                                    result_file.write("\n")
                                    result_file.write(
                                        "Category: {0}".format(str(output["results"][17]["categoryTitle"] + "\n")))
                                    result_file.write("Title: {0}".format(str(output["results"][17]["title"] + "\n")))
                                    result_file.write("Vicinity: {0}".format(
                                        str(output["results"][17]["vicinity"]).replace("<br/>", "") + "\n"))
                                    result_file.write(
                                        "Result type: {0}".format(str(output["results"][17]["resultType"] + "\n")))
                                    result_file.write("\n")
                                    result_file.write(
                                        "Category: {0}".format(str(output["results"][18]["categoryTitle"] + "\n")))
                                    result_file.write("Title: {0}".format(str(output["results"][18]["title"] + "\n")))
                                    result_file.write("Vicinity: {0}".format(
                                        str(output["results"][18]["vicinity"]).replace("<br/>", "") + "\n"))
                                    result_file.write(
                                        "Result type: {0}".format(str(output["results"][18]["resultType"] + "\n")))
                                    result_file.write("\n")
                                    result_file.write(
                                        "Category: {0}".format(str(output["results"][19]["categoryTitle"] + "\n")))
                                    result_file.write("Title: {0}".format(str(output["results"][19]["title"] + "\n")))
                                    result_file.write("Vicinity: {0}".format(
                                        str(output["results"][19]["vicinity"]).replace("<br/>", "") + "\n"))
                                    result_file.write(
                                        "Result type: {0}".format(str(output["results"][19]["resultType"] + "\n")))

                                    print("Output saved as Output.txt")
                                    engine.say("Output saved as Output.txt")
                                    engine.runAndWait()

                                    result_file.close()
                                    break
                            else:
                                print("Searched for " + str(place).title() + " successfully.")
                                engine.say("Searched for " + str(place)) + " successfully."
                                engine.runAndWait()

                except sr.UnknownValueError:
                    print("Could not recognize audio input. Please try again")
                    engine.say("Could not recognize audio input. Please try again.")
                    engine.runAndWait()

                except sr.RequestError:
                    engine.say(" ")
                    engine.runAndWait()

                except sr.WaitTimeoutError:
                    print("Please try again.")
                    engine.say(" ")
                    engine.runAndWait()

        # MEDIA

        elif "play music" in recognizer1.recognize_google(audio, language="en-US"):

            print("Initializing Zira's Music Player...")
            engine.say("Initializing Zira's Music Player...")
            engine.runAndWait()
            print("Music Player initialized!")
            engine.say("Music Player initialized!")
            engine.runAndWait()
            print("What song do you want to listen to, operator?")
            engine.say("What song do you want to listen to, operator?")
            engine.runAndWait()

            while True:
                with sr.Microphone() as src:
                    audio5 = recognizer1.listen(src, timeout=1, phrase_time_limit=5)

                try:
                    for files in os.listdir("C:\\Zira\\Music"):  # iterate in each file in Downloads folder
                        if recognizer1.recognize_google(audio5, language="en-US") in files:
                            print("Now playing " + os.path.basename(files))  # THIS WORKS PERFECTLY
                            engine.say("Now playing " + os.path.basename(files))  # THIS WORKS PERFECTLY
                            engine.runAndWait()

                            files_type = os.path.splitext(files)

                            if files_type[0] == recognizer1.recognize_google(audio5, language="en-US"):
                                mixer.music.load("C:\\Zira\\Music\\" + files)
                                mixer.music.play()

                                while mixer.music.get_busy():
                                    time.Clock().tick(10)

                                    with sr.Microphone() as src:
                                        audio6 = recognizer1.listen(src, timeout=1, phrase_time_limit=5)

                                    try:
                                        if "pause" in recognizer1.recognize_google(audio6, language="en-US"):
                                            mixer.music.pause()
                                            print("Music paused.")
                                            engine.say("Music paused.")
                                            engine.runAndWait()

                                        elif "resume" in recognizer1.recognize_google(audio6, language="en-US"):
                                            print("Resuming music...")
                                            engine.say("Resuming music...")
                                            engine.runAndWait()
                                            mixer.music.unpause()

                                        elif "stop" in recognizer1.recognize_google(audio6, language="en-US"):
                                            mixer.music.stop()
                                            print("Music stopped.")
                                            engine.say("Music stopped.")
                                            engine.runAndWait()
                                            break

                                        elif "mute" in recognizer1.recognize_google(audio6, language="en-US"):
                                            mixer.music.set_volume(0)
                                            print("Music muted.")
                                            engine.say("Music muted.")
                                            engine.runAndWait()

                                        elif "unmute" in recognizer1.recognize_google(audio6, language="en-US"):
                                            print("Music unmuted.")
                                            engine.say("Music unmuted.")
                                            engine.runAndWait()
                                            mixer.music.set_volume(1)

                                        else:
                                            print("I cannot recognize your command. Please try again.")
                                            engine.say("I cannot recognize your command. Please try again.")
                                            engine.runAndWait()

                                    except sr.UnknownValueError:
                                        engine.say(" ")
                                        engine.runAndWait()

                                    except sr.RequestError:
                                        print("Unstable internet connection. Please try again.")
                                        engine.say("Unstable internet connection. Please try again.")
                                        engine.runAndWait()
                            else:
                                print("Music not found. Please try again.")
                                engine.say("Music not found. Please try again")
                                engine.runAndWait()

                except sr.UnknownValueError:
                    engine.say(" ")
                    engine.runAndWait()

                except sr.RequestError:
                    engine.say(" ")
                    engine.runAndWait()

                except sr.WaitTimeoutError:
                    print("Please try again.")
                    engine.say(" ")
                    engine.runAndWait()

        elif "take a picture" in recognizer1.recognize_google(audio, language="en-US"):
            take_picture()

        elif "record a video" in recognizer1.recognize_google(audio, language="en-US"):
            print("Initializing Webcam...")
            engine.say("Initializing webcam...")
            engine.runAndWait()
            print("Webcam initialized!")
            engine.say("Webcam initialized")
            engine.runAndWait()
            print("Please press the escape key to end the recording.")
            engine.say("Please press the escape key to end the recording.")
            engine.runAndWait()
            print("PS. Your previous video will be overwritten if not renamed or copied.")
            engine.say("PS. Your previous video will be overwritten if not renamed or copied.")
            engine.runAndWait()
            print("The output file name is Video.avi.")
            engine.say("The output file name is Video.avi")
            engine.runAndWait()
            if __name__ == '__main__':
                main()
            print("Webcam shut down.")
            engine.say("Webcam shut down")
            engine.runAndWait()

        # SPICE

        elif "random number" in recognizer1.recognize_google(audio, language="en-US"):
            result = random.randint(0, 100)
            print("Randomizing a number...")
            engine.say("Randomizing a number...")
            engine.runAndWait()
            print("Your lucky number is " + str(result))
            engine.say("Your lucky number is " + str(result))
            engine.runAndWait()

        elif "toss a coin" in recognizer1.recognize_google(audio, language="en-US"):
            coin = ["HEADS", "TAILS"]
            result = random.choice(coin)
            print("Tossing a coin...")
            engine.say("Tossing a coin...")
            engine.runAndWait()
            winsound.PlaySound(resource_path("coin_toss.wav"), winsound.SND_FILENAME)
            print("The coin toss shows " + str(result))
            engine.say("The coin toss shows" + str(result))
            engine.runAndWait()

        elif "roll a die" in recognizer1.recognize_google(audio, language="en-US"):
            result = random.randint(1, 6)
            print("Rolling a die...")
            engine.say("Rolling a die")
            engine.runAndWait()
            winsound.PlaySound(resource_path("roll_die.wav"), winsound.SND_FILENAME)
            print("The die result shows " + str(result))
            engine.say("The die result shows " + str(result))
            engine.runAndWait()

        # EXIT

        elif "shutdown" in recognizer1.recognize_google(audio, language='en-US'):
            print("Thank you for your time, operator!")
            engine.say("Thank you for your time, operator!")
            engine.runAndWait()
            print("Zira, shutting down..")
            engine.say("Zira, shutting down...")
            engine.runAndWait()
            sys.exit()

        # EXCEPTIONS

        else:
            print("I don't recognize your command. Please try again")
            engine.say("I don't recognize your command. Please try again")
            engine.runAndWait()

    except sr.UnknownValueError:
        print("Could not recognize audio input. Please try again")
        engine.say("Could not recognize audio input. Please try again")
        engine.runAndWait()

    except sr.RequestError:
        print("Please check your internet connection and try again.")
        engine.say("Please check your internet connection and try again.")
        engine.runAndWait()

    except sr.WaitTimeoutError:
        print("Listening timed out while waiting for phrase to start. Please try again.")
        engine.say("Listening timed out while waiting for phrase to start. Please try again.")
        engine.runAndWait()
