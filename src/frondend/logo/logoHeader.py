import PySimpleGUI as sg


def zwrocOkno(param, layout):
    logo = sg.Image('src/obrazy/logo/logo.png')
    print(layout)
    layout[0].insert(0, logo)
    print(layout)
    return sg.Window(param, layout)
