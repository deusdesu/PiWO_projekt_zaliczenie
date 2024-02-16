import PySimpleGUI as sg

from frondend.konfiuguracja.theme.theme import globalTheme


def poleTytulowe3():
    return sg.Text('Dodanie nowego samochodu',
                   key='dodNowegoSampochodu',
                   font='Franklin 26',
                   pad=(10, 20)
                   )


def okno3():
    sg.theme(globalTheme)
    sg.set_options(font='Calibri 14', button_element_size=(6, 3))
    # button_size = (6, 3)
    layout = [
        [poleTytulowe3()],
        [sg.Text('Marka samochodu '), sg.Push(), sg.Input(key='Name1')],
        [sg.Text('Model samochodu '), sg.Push(), sg.Input(key='Name2')],
        [sg.Text('Kolor '), sg.Push(), sg.Input(key='Name2')],
        [sg.Text('Numer rejestracyjny '), sg.Push(), sg.Input(key='Name2')],
        [sg.Text('Numer VIN '), sg.Push(), sg.Input(key='Name2')],
        [sg.Text('data ubezpieczenia początek'), sg.Push(), sg.Input(key='Name2')],
        [sg.Text('data ubezpieczenia koniec'), sg.Push(), sg.Input(key='Name2')],
        [sg.Text('Ubezpieczyciel '), sg.Push(), sg.Input(key='Name2')],
        [sg.Text('Nr polisy '), sg.Push(), sg.Input(key='Name2')],
        [sg.Text('poprzedni przegląd techniczny '), sg.Push(), sg.Input(key='Name2')],
        [sg.Text('następny przegląd techniczny '), sg.Push(), sg.Input(key='Name2')],
        [sg.Text('stan własności '), sg.Push(), sg.Input(key='Name2')],
        [sg.Text('przebieg '), sg.Push(), sg.Input(key='Name2')],
        [sg.Text('obecna lokalizacja '), sg.Push(), sg.Input(key='Name2')],
        [sg.Text('status samochodu '), sg.Push(), sg.Input(key='Name2')],
        [sg.Text('typ paliwa '), sg.Push(), sg.Input(key='Name2')],
        [sg.Text('średnie spalanie L/100km'), sg.Push(), sg.Input(key='Name2')],
        [sg.Text('skrzynia biegów '), sg.Push(), sg.Input(key='Name2')],
        [sg.Text('dystans do przejechania '), sg.Push(), sg.Input(key='Name2')],

        [sg.OK(key='OKOkno3'), sg.Button('Powrót', key='powrot', expand_x=True)],

    ]
    return sg.Window('Converter', layout)
