import PySimpleGUI as sg

from src.Repozytorium.bazaDanychStrategy.enumPath import KIEROWCA_PATH
from src.backend.servis.abstract.abstractCrateTable import create_table_from_database
from src.frondend.konfiuguracja.theme.theme import globalTheme
from src.frondend.logo.logoHeader import zwrocOkno

def poleTytulowe6():
    return sg.Text('Przegląd kierowców',
                   key='Przegladkierowcow',
                   font='Franklin 26',
                   pad=(10, 20)
                   )


def okno6():
    sg.theme(globalTheme)
    sg.set_options(font='Calibri 14', button_element_size=(6, 3))
    # button_size = (6, 3)
    layout = [
        [poleTytulowe6()],

        create_table_from_database(KIEROWCA_PATH),

        [sg.OK(key='OKOkno6', size=(20, 1)), sg.Push(), sg.Button('Powrót', key='powrot', size=(20, 1) )],

    ]
    return zwrocOkno('Converter', layout)