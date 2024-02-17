import PySimpleGUI as sg
from src.frondend.konfiuguracja.theme.theme import globalTheme


def poleTytulowe2():
    return sg.Text('Okno decyzji'.center(30),
                   key='oknoDecyzji',
                   font='Franklin 26',
                   pad=(10, 20),
                   justification='center'
                   )



def okno2():
    sg.theme(globalTheme)
    sg.set_options(font='Calibri 14', button_element_size=(6, 3))
    # button_size = (6, 3)
    layout = [
        [poleTytulowe2()],
        [sg.Button('Dodaj nowy samochód', key='3', size=(20, 1)), sg.Push(),
         sg.Button('Dodaj nowego kierowcę', key='4', size=(20, 1))],
        [sg.Button('Przegląd floty', key='5', size=(20, 1)), sg.Push(),
         sg.Button('Przegląd kierowców', key='6', size=(20, 1))],
        [sg.Button('Serwis', key='9', size=(20, 1)), sg.Push(), sg.Button('Zgłoś usterkę', key='10', size=(20, 1))],
        [sg.Button('Podjęcie samochodu', key='7', size=(20, 1)), sg.Push(),
         sg.Button('Zwrot samochodu', key='8', size=(20, 1))],

    ]
    return sg.Window('Converter', layout)
