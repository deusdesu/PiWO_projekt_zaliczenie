import PySimpleGUI as sg

from frondend.konfiuguracja.theme.theme import globalTheme


def poleTytulowe4():
    return sg.Text('Dodanie nowego kierowcy',
                   key='dodNowegoKierowcy',
                   font='Franklin 26',
                   pad=(10, 20)
                   )


def okno4():
    sg.theme(globalTheme)
    sg.set_options(font='Calibri 14', button_element_size=(6, 3))
    # button_size = (6, 3)
    layout = [
        [poleTytulowe4()],
        [sg.Text('Imię '), sg.Push(), sg.Input(key='ImieKierowcy')],
        [sg.Text('Nazwisko '), sg.Push(), sg.Input(key='NazwiskoKierowcy')],
        [sg.Text('Data urodzenia '), sg.Push(), sg.Input(key='DataUrodzeniaKierowcy')],
        [sg.Text('Kategorie prawa jazdy '), sg.Push(), sg.Input(key='KategoriePJKierowcy')],
        [sg.Text('Termin ważności PJ Od '), sg.Push(), sg.Input(key='TerwinWaznosciPJOd')],
        [sg.Text('Termin ważności PJ Do'), sg.Push(), sg.Input(key='TerminWaznosciPJDo')],
        [sg.Text('Adres zamieszkania '), sg.Push(), sg.Input(key='AdresZamieszkaniaKierowcy')],
        [sg.Text('Miejscowość '), sg.Push(), sg.Input(key='MiejscowoscKierowcy')],
        [sg.Text('Kod pocztowy '), sg.Push(), sg.Input(key='KodPocztowyKierowcy')],


        [sg.OK(key='OKOkno4', size=(20, 1)), sg.Push(), sg.Button('Powrót', key='powrot', size=(20, 1) )],

    ]
    return sg.Window('Converter', layout)
