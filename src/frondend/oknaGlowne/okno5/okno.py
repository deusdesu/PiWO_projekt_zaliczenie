# -*- coding: utf-8 -*-
import PySimpleGUI as sg

from src.Repozytorium.bazaDanychStrategy.enumPath import SAMOCHOD_PATH
from src.backend.servis.abstract.abstractCrateTable import create_table_from_database
from src.frondend.konfiuguracja.theme.theme import globalTheme


def poleTytulowe5():
    return sg.Text('Przegląd floty',
                   key='PrzegladFloty',
                   font='Franklin 26',
                   pad=(10, 20)
                   )


def okno5():
    sg.theme(globalTheme)
    sg.set_options(font='Calibri 14', button_element_size=(6, 3))
    # button_size = (6, 3)

    layout = [
        [poleTytulowe5()],
        create_table_from_database(SAMOCHOD_PATH),


        [sg.OK(key='OKOkno5', size=(20, 1)), sg.Push(), sg.Button('Powrót', key='powrot', size=(20, 1) )],

    ]
    return sg.Window('Converter', layout)