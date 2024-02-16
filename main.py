import PySimpleGUI as sg

theme_menu = ['menu',
              ['BrightColors',
               'Dark',
               'BlueMono',
               'HotDogStand',
               'random hehe',
               ]
              ]

globalTheme = 'Black'


def okno2():
    sg.theme(globalTheme)
    sg.set_options(font='Calibri 14', button_element_size=(6, 3))
    # button_size = (6, 3)
    layout = [
        [poleTytulowe2()],
        [sg.Button('Dodaj nowy samochód', key='3', expand_x=True),
         sg.Button('Dodaj nowego kierowcę', key='4', expand_x=True)],
        [sg.Button('Przegląd floty', key='5', expand_x=True), sg.Button('Przegląd kierowców', key='6', expand_x=True)],
        [sg.Button('Serwis', key='9', expand_x=True), sg.Button('Zgłoś usterkę', key='10', expand_x=True)],
        [sg.Button('Podjęcie samochodu', key='7', expand_x=True), sg.Button('Zwrot samochodu', key='8', expand_x=True)],

    ]
    return sg.Window('Converter', layout)


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
        [sg.Button('Powrót', key='powrot', expand_x=True)],
        [sg.Text('Name '),  sg.Input(key='Name1')],
        [sg.Text('Name '), sg.Input(key='Name2')],
        [sg.OK(key='OKOkno3')]

    ]
    return sg.Window('Converter', layout)


def poleTytulowe2():
    return sg.Text('Okno decyzji',
                   key='oknoDecyzji',
                   font='Franklin 26',
                   pad=(10, 20)
                   )


def start():
    window = okno2()

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        window = okno2Przyciski(event, window)
        test(event, values)
    window.close()


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
    if event == 'powrot':
        window.close()  # Zamknij aktualne okno (okno2)
        window = okno2()  # Otwórz okno3 jako nowe okno
    return window


def test(event, values):
    if event == 'OKOkno3':
        print(values)


if __name__ == '__main__':
    start()
