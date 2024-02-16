import PySimpleGUI as sg
from frondend.konfiuguracja.theme.theme import globalTheme


def poleTytulowe2():
    return sg.Text('Okno decyzji',
                   key='oknoDecyzji',
                   font='Franklin 26',
                   pad=(10, 20)
                   )


def okno2():
    sg.theme(globalTheme)
    sg.set_options(font='Calibri 14', button_element_size=(6, 3))
    # button_size = (6, 3)
    layout = [
        [poleTytulowe2()],
        [sg.Button('Dodaj nowy samochód', key='3', expand_x=True),
         sg.Button('Dodaj nowego kierowcę', key='4', expand_x=True)],
        [sg.Button('Przegląd floty', key='5', expand_x=True), sg.Button('Przegląd kierowców', key='6', expand_x=True)],
        [sg.Button('Serwis', key='9', expand_x=True), sg.Button('Zgłoś usterkę', key='10', expand_x=True)],
        [sg.Button('Podjęcie samochodu', key='7', expand_x=True), sg.Button('Zwrot samochodu', key='8', expand_x=True)],

    ]
    return sg.Window('Converter', layout)
