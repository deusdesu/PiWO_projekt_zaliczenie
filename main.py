# -*- coding: utf-8 -*-
import PySimpleGUI as sg

from Repozytorium.bazaDanychStrategy.enumPath import SAMOCHOD_PATH, KIEROWCA_PATH
from backend.servis.abstractCrateTable import create_table
from backend.servis.abstractDodajDaneServices import add_data_from_json
from frondend.oknaGlowne.okno10.okno import okno10
from frondend.oknaGlowne.okno2.okno import okno2
from frondend.oknaGlowne.okno3.okno import okno3
from frondend.oknaGlowne.okno4.okno import okno4
from frondend.oknaGlowne.okno5.okno import okno5
from frondend.oknaGlowne.okno6.okno import okno6
from frondend.oknaGlowne.okno7.okno import okno7
from frondend.oknaGlowne.okno8.okno import okno8
from frondend.oknaGlowne.okno9.okno import okno9


def start():
    window = okno2()

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        window = okno2Przyciski(event, window)
        window = okno3Obsluga(event, values, window)
        window = okno4Obsluga(event, values, window)
        # window = okno5Obsluga(event, window)
        window = przyciskPowrot(event, window)

    window.close()


def przyciskPowrot(event, window):
    if event == 'powrot':
        window = powrotDoOknaGlownego(window)
    return window


def powrotDoOknaGlownego(window):
    window.close()  # Zamknij aktualne okno (okno2)
    window = okno2()  # Otwórz okno3 jako nowe okno
    return window


def okno2Przyciski(event, window):
    if event == '3':
        print('Dodaj nowy samochód')
        window.close()  # Zamknij aktualne okno (okno2)
        window = okno3()  # Otwórz okno3 jako nowe okno
    if event == '4':
        print('Dodaj nowego kierowcę')
        window.close()  # Zamknij aktualne okno (okno4)
        window = okno4()  # Otwórz okno4 jako nowe okno
    if event == '5':
        print('Przegląd floty')
        window.close()  # Zamknij aktualne okno (okno5)
        window = okno5()  # Otwórz okno5 jako nowe okno
    if event == '6':
        print('Przegląd kierowców')
        window.close()  # Zamknij aktualne okno (okno6)
        window = okno6()  # Otwórz okno6 jako nowe okno
    if event == '7':
        print('Podjęcie samochodu')
        window.close()  # Zamknij aktualne okno (okno7)
        window = okno7()  # Otwórz okno6 jako nowe okno
    if event == '8':
        print('Zwrot samochodu')
        window.close()  # Zamknij aktualne okno (okno8)
        window = okno8()  # Otwórz okno6 jako nowe okno
    if event == '9':
        print('Serwis')
        window.close()  # Zamknij aktualne okno (okno8)
        window = okno9()  # Otwórz okno6 jako nowe okno
    if event == '10':
        print('Zgłoś usterkę')
        window.close()  # Zamknij aktualne okno (okno8)
        window = okno10()  # Otwórz okno6 jako nowe okno
    return window


def okno3Obsluga(event, values, window):
    if event == 'OKOkno3':
        add_data_from_json(values, SAMOCHOD_PATH)
        print(values)
        window = powrotDoOknaGlownego(window)
    return window


def okno4Obsluga(event, values, window):
    if event == 'OKOkno4':
        add_data_from_json(values, KIEROWCA_PATH)
        print(values)
        window = powrotDoOknaGlownego(window)
    return window


if __name__ == '__main__':
    start()
