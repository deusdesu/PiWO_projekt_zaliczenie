import PySimpleGUI as sg

from frondend.konfiuguracja.theme.theme import globalTheme


def poleTytulowe9():
    return sg.Text('Serwis',
                   key='Serwis',
                   font='Franklin 26',
                   pad=(10, 20),
                   justification='center'
                   )


def okno9():
    sg.theme(globalTheme)
    sg.set_options(font='Calibri 14', button_element_size=(6, 3))
    # button_size = (6, 3)
    layout = [
        [poleTytulowe9()],
        [sg.Text('Podaj numer samochodu naprawionego '), sg.Input(key='NaprawionySamochod'), sg.Ok(key='OKOkno9', size=(20, 1))],



        [ sg.Push(), sg.Button('Powrót', key='powrot', size=(20, 1))],

    ]
    return sg.Window('Converter', layout)