import PySimpleGUI as sg

from frondend.konfiuguracja.theme.theme import globalTheme


def poleTytulowe7():
    return sg.Text('Podjęcie samochodu',
                   key='dodNowegoKierowcy',
                   font='Franklin 26',
                   pad=(10, 20)
                   )


def okno7():
    sg.theme(globalTheme)
    sg.set_options(font='Calibri 14', button_element_size=(6, 3))
    # button_size = (6, 3)
    layout = [
        [poleTytulowe7()],
        [sg.Text('Podaj numer kierowcy '), sg.Push(), sg.Input(key='NumerKierowcy')],
        [sg.Text('Podaj numer samochodu '), sg.Push(), sg.Input(key='NumerSamochodu')],
        [sg.Text('Planowany powrót '), sg.Push(), sg.Input(key='DataPowrotu')],



        [sg.Button('Podejmij' ,key='OKOkno7', size=(20, 1)), sg.Push(), sg.Button('Powrót', key='powrot', size=(20, 1) )],

    ]
    return sg.Window('Converter', layout)