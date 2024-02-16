import PySimpleGUI as sg

from backend.servis.samochodServis import add_car_from_json
from frondend.oknaGlowne.okno2.okno import okno2
from frondend.oknaGlowne.okno3.okno import okno3


def start():
    window = okno2()

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        window = okno2Przyciski(event, window)
        window = okno3Obsluga(event, values, window)
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
    if event == '5':
        print('Przegląd floty')
    if event == '6':
        print('Przegląd kierowców')
    if event == '7':
        print('Podjęcie samochodu')
    if event == '8':
        print('Zwrot samochodu')
    if event == '9':
        print('Serwis')
    if event == '10':
        print('Zgłoś usterkę')
    return window


def okno3Obsluga(event, values, window):
    if event == 'OKOkno3':
        add_car_from_json(values)
        print(values)
        powrotDoOknaGlownego(window)
    return window
if __name__ == '__main__':
    start()
