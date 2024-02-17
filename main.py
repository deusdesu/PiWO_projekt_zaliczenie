# -*- coding: utf-8 -*-
import PySimpleGUI as sg

from src.Repozytorium.bazaDanychStrategy.enumPath import SAMOCHOD_PATH, KIEROWCA_PATH
from src.Repozytorium.bazaDanychStrategy.enumStatusSamochodu import ENUM_W_UZYCIU, ENUM_DOSTEPNY
from src.backend.servis.abstract.abstractDodajDaneServices import add_data_from_json
from src.backend.servis.serwisSerwis.serwis import obsluga_zglos_usterke, obsluga_usun_usterke, zmiana_dodanie_kierowcy, \
    zmiana_statusu
from src.frondend.oknaGlowne.okno10.okno import okno10
from src.frondend.oknaGlowne.okno2.okno import okno2
from src.frondend.oknaGlowne.okno3.okno import okno3
from src.frondend.oknaGlowne.okno4.okno import okno4
from src.frondend.oknaGlowne.okno5.okno import okno5
from src.frondend.oknaGlowne.okno6.okno import okno6
from src.frondend.oknaGlowne.okno7.okno import okno7
from src.frondend.oknaGlowne.okno8.okno import okno8
from src.frondend.oknaGlowne.okno9.okno import okno9


def start():
    window = okno2()

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        window = okno2Przyciski(event, window)
        window = okno3Obsluga(event, values, window)
        window = okno4Obsluga(event, values, window)
        window = okno7Obsluga(event, values, window)
        window = okno10Obsluga(event, values, window)
        window = okno8Obsluga(event, values, window)
        window = okno8ObslugaUsterka(event, window)
        window = okno9przyciskUsunUsterke(event, values, window)
        # window = okno5Obsluga(event, window)
        window = przyciskPowrot(event, window)
    window.close()


def przyciskPowrot(event, window):
    if event == 'powrot':
        window = przejdzDoOknaGlownego(window)
    return window


def przejdzDoOknaGlownego(window):
    window.close()  # Zamknij aktualne okno (okno2)
    window = okno2()  # Otwórz okno3 jako nowe okno
    return window


def przejdzDoFlotyPojazdow(window):
    window.close()  # Zamknij aktualne okno (okno2)
    window = okno5()  # Otwórz okno3 jako nowe okno
    return window


def przejdzZglosUsterke(window):
    window.close()  # Zamknij aktualne okno (okno2)
    window = okno10()  # Otwórz okno3 jako nowe okno
    return window


def okno2Przyciski(event, window):
    if event == '3':
        window.close()  # Zamknij aktualne okno (okno2)
        window = okno3()  # Otwórz okno3 jako nowe okno
    if event == '4':
        window.close()  # Zamknij aktualne okno (okno4)
        window = okno4()  # Otwórz okno4 jako nowe okno
    if event == '5':
        window.close()  # Zamknij aktualne okno (okno5)
        window = okno5()  # Otwórz okno5 jako nowe okno
    if event == '6':
        window.close()  # Zamknij aktualne okno (okno6)
        window = okno6()  # Otwórz okno6 jako nowe okno
    if event == '7':
        window.close()  # Zamknij aktualne okno (okno7)
        window = okno7()  # Otwórz okno6 jako nowe okno
    if event == '8':
        window.close()  # Zamknij aktualne okno (okno8)
        window = okno8()  # Otwórz okno6 jako nowe okno
    if event == '9':
        window.close()  # Zamknij aktualne okno (okno8)
        window = okno9()  # Otwórz okno6 jako nowe okno
    if event == '10':
        window.close()  # Zamknij aktualne okno (okno8)
        window = okno10()  # Otwórz okno6 jako nowe okno
    return window


def okno3Obsluga(event, values, window):
    if event == 'OKOkno3':
        add_data_from_json(values, SAMOCHOD_PATH)
        window = przejdzDoOknaGlownego(window)
    return window


def okno4Obsluga(event, values, window):
    if event == 'OKOkno4':
        add_data_from_json(values, KIEROWCA_PATH)
        window = przejdzDoOknaGlownego(window)
    return window


def okno10Obsluga(event, values, window):
    if event == 'OKOkno10':
        obsluga_zglos_usterke(values)
        window = przejdzDoFlotyPojazdow(window)
    return window


def okno9przyciskUsunUsterke(event, values, window):
    if event == 'OKOkno9':
        obsluga_usun_usterke(values)
        window = przejdzDoFlotyPojazdow(window)
    return window


def okno7Obsluga(event, values, window):
    if event == 'OKOkno7':
        zmiana_dodanie_kierowcy(values['NumerSamochodu'], values['NumerKierowcy'], values['DataPowrotu'])
        zmiana_statusu(values['NumerSamochodu'], ENUM_W_UZYCIU)
        window = przejdzDoFlotyPojazdow(window)
    return window


def okno8Obsluga(event, values, window):
    if event == 'OKOkno8':
        zmiana_dodanie_kierowcy(values['NumerSamochodu'], '', '')
        zmiana_statusu(values['NumerSamochodu'], ENUM_DOSTEPNY)
        window = przejdzDoFlotyPojazdow(window)
    return window


def okno8ObslugaUsterka(event, window):
    if event == 'ZglosUsterke':
        window = przejdzZglosUsterke(window)
    return window


if __name__ == '__main__':
    start()
