import PySimpleGUI as sg


def zwrocOkno(param, layout):
    logo = sg.Image('src/obrazy/logo/logo.png')
    layout[0].insert(0, logo)
    return sg.Window(param, layout)
