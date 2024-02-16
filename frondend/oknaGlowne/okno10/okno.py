import PySimpleGUI as sg

from frondend.konfiuguracja.theme.theme import globalTheme


def poleTytulowe10():
    return sg.Text('Zgłaszanie usterki',
                   key='zglaszanieusterki',
                   font='Franklin 26',
                   pad=(10, 20),
                   justification='center'
                   )


def okno10():
    sg.theme(globalTheme)
    sg.set_options(font='Calibri 14', button_element_size=(6, 3))
    # button_size = (6, 3)
    layout = [
        [poleTytulowe10()],
        [sg.Text('Podaj numer samochodu '), sg.Push(), sg.Input(key='Numersamochodu')],
        [sg.Text('Usterka '), sg.Push(), sg.Input(key='Usterka')],



        [sg.Button('Podejmij' ,key='OKOkno10', size=(20, 1)), sg.Push(), sg.Button('Powrót', key='powrot', size=(20, 1) )],

    ]
    return sg.Window('Converter', layout)