#from Python_Magnet_Sim import *
from functions import *
import PySimpleGUI as sg


def file_interpreter(file):
    file = open(file, "r+")
    content = file.read()
    exec(content)

layout = [
          [sg.Text('GUI Interpreter', text_color='black', background_color='pink')],   
          [sg.Text('File to interpret' , justification='left' ,text_color='black', background_color='pink'),
           sg.InputText('',key='file_to_interpret',text_color='black', background_color='pink'), sg.FileBrowse()],
          [sg.Button('Interpret', button_color=('white', 'blue')), sg.Button('Exit', button_color=('white', 'blue'))]
         ]      


window = sg.Window('MagnetScript Interpreter', layout, background_color="pink", icon = "icon.ico")

while True:
  event, values = window.Read()
  if event == 'Interpret':
    file_interpreter(values['file_to_interpret'])
  elif event == 'Exit':
    break

window.Close()
raise Exception('You exited bro')
