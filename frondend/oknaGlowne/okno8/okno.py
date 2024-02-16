import PySimpleGUI as sg

from frondend.konfiuguracja.theme.theme import globalTheme


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
        [sg.Text('Podaj numer samochodu '), sg.Push(), sg.Input(key='NumerKierowcy')],
        [sg.Text('Podaj liczbę przejechanych kilometrów '), sg.Push(), sg.Input(key='NumerSamochodu')],

        [sg.Button('Zgłoś usterkę' ,key='Usterka3', size=(20, 1))],


        [sg.Button('Zdaj' ,key='OKOkno8', size=(20, 1)), sg.Push(), sg.Button('Powrót', key='powrot', size=(20, 1) )],

    ]
    return sg.Window('Converter', layout)