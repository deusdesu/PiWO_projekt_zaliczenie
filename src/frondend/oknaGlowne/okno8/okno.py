import PySimpleGUI as sg

from src.frondend.konfiuguracja.theme.theme import globalTheme
from src.frondend.logo.logoHeader import zwrocOkno

def poleTytulowe8():
    return sg.Text('Zdanie samochodu',
                   key='ZdanieSamochodu',
                   font='Franklin 26',
                   pad=(10, 20)
                   )


def okno8():
    sg.theme(globalTheme)
    sg.set_options(font='Calibri 14', button_element_size=(6, 3))
    # button_size = (6, 3)
    layout = [
        [poleTytulowe8()],
        [sg.Text('Podaj numer samochodu '), sg.Push(), sg.Input(key='NumerSamochodu')],
        [sg.Text('Podaj liczbę przejechanych kilometrów '), sg.Push(), sg.Input(key='przejechaneKilometry')],

        [sg.Button('Zgłoś usterkę' ,key='ZglosUsterke', size=(20, 1))],


        [sg.Button('Zdaj' ,key='OKOkno8', size=(20, 1)), sg.Push(), sg.Button('Powrót', key='powrot', size=(20, 1) )],

    ]
    return zwrocOkno('Converter', layout)