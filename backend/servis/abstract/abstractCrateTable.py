# -*- coding: utf-8 -*-
import PySimpleGUI as sg

from Repozytorium.zarzadzanieFlotaPojazdow.abstractRepository import read_csv


def generate_table(data):
    if not data:
        return []
    headings = list(data[0].keys())
    values = [[row[heading] for heading in headings] for row in data]

    layout = [sg.Table(values=values, headings=headings, auto_size_columns=False,
                       justification='right', display_row_numbers=False,
                       num_rows=min(25, len(data)))],

    return layout


def create_table(PATH):
    return generate_table(read_csv(PATH))
