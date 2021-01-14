import PySimpleGUI as sg
import requests
import wikipedia
import os

# import pyttsx3
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)

import wolframalpha
appID = ""
userName = ""

sg.theme('DarkRed2')   
# All the stuff inside your window.
layout = [  [sg.Text('Hello ' + userName + ', I am your virtual assistant. What would you like to know...')],
            [sg.Text('Search', font=("Helvetica", 25)), sg.InputText()],
            [sg.Button('Ok', font=("Helvetica", 15)), sg.Button('Cancel', font=("Helvetica", 15))] ]

# Create the Window
window_main = sg.Window(userName + ' Virtual Assistant', layout)

# Initial Greeting
os.system("/usr/bin/say Hello, I am your virtual assistant. What would you like to know?")

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window_main.read()
    
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break    

    try:
        wiki_res = wikipedia.summary(values[0], sentences=1)

        split_input = values[0].split()
        search_input = '+'.join(split_input)
        url = f"http://api.wolframalpha.com/v1/result?appid={appID}&i={search_input}%3F"
        wolfram_res = requests.get(url)

        # engine.say(wolfram_res.text)
        # engine.runAndWait()
        os.system("/usr/bin/say " + wolfram_res.text)
        sg.PopupNonBlocking(wolfram_res.text + "\n\n\n" + wiki_res)
        os.system("/usr/bin/say " + "What else would you like to know?")
    except:
        sg.PopupNonBlocking("Invalid request!")
        os.system("/usr/bin/say Sorry, I could not find an answer for you")
     
window_main.close()
