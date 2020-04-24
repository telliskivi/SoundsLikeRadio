import random
import time
from playsound import playsound
import PySimpleGUI as sg
import time

sg.ChangeLookAndFeel('TealMono') #värv

#graafika liides
layout = [
    [sg.Text(' ')],       
    [sg.Text('_'  * 81)],          
    [sg.Button("Play/Stop"), sg.Text('', size=(23, 1), font=('Helvetica', 20), justification='center', key='_OUTPUT_')]]


window = sg.Window('SoundsLikeRadio', default_element_size=(10, 10), auto_size_buttons=False).Layout(layout)
vajutus = False

while True:                          
    event, values = window.read(timeout=10) 
    if event in (None, 'Quit'):          
        break
    elif event == 'Play/Stop': #nupuvajutus käivitab programmi
        vajutus = not vajutus
    if vajutus:
        #randoming mängib suvalise aja tagant suvalist faili
        list_mp3 = ['intro.mp3','koit.mp3'] #milliseid helifaile võib kuulda
        playsound(random.choice(list_mp3))
        time.sleep(random.randint(2,10))
            
                
