import random
import time
from playsound import playsound
import PySimpleGUI as sg
import time

sg.ChangeLookAndFeel('DarkAmber') #värv

layout = [
    [sg.Text(' ')], #ülesse jääb tühi osa       
    [sg.Text('_'  * 81)], #ilu pärast lisatud vahe joon            
    [sg.Button("Play/Stop"), sg.Text('', size=(23, 1), font=('Helvetica', 20), justification='center', key='_OUTPUT_')] #osa, kus hakkavad sekundid jooksma
]

window = sg.Window('Raadio 2', default_element_size=(40, 20), auto_size_buttons=False).Layout(layout)
aeg_jookseb, counter = False, 0

while True:                          
    event, values = window.read(timeout=10) 
    if event in (None, 'Quit'):          
        break
    elif event == 'Play/Stop': #nupuvajutus käivitab programmi
        aeg_jookseb = not aeg_jookseb
    if aeg_jookseb:
        while True: #randoming mängib suvalise aja tagant suvalist faili
            list_mp3 = ['intro.mp3','koit.mp3'] #milliseid helifaile võib kuulda
            playsound(random.choice(list_mp3))
            time.sleep(random.randint(2,10))
