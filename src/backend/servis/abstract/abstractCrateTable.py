# -*- coding: utf-8 -*-
import PySimpleGUI as sg

from src.Repozytorium.bazaDanychStrategy.enumPath import SERWIS_PATH, SAMOCHOD_PATH
from src.Repozytorium.zarzadzanieFlotaPojazdow.abstractRepository import read_csv


def generate_table_from_database(data):
    if not data:
        return []
    headings = list(data[0].keys())
    values = [[row[heading] for heading in headings] for row in data]

    layout = [sg.Table(values=values, headings=headings, auto_size_columns=False,
                       justification='right', display_row_numbers=False,
                       num_rows=min(25, len(data)))],

    return layout


def create_table_from_database(PATH):
    return generate_table_from_database(read_csv(PATH))


def podajDaneTegoAuta(idSamochodu, samochod_dane):
    for row in samochod_dane:
        if row['Id'] == idSamochodu:
            return row['MarkaSamochodu'], row['ModelSamochodu'], row['NumerRejestracyjny']


def generate_table_from_json():
    serwis_dane = read_csv(SERWIS_PATH)
    samochod_dane = read_csv(SAMOCHOD_PATH)

    for row in serwis_dane:
        marka, model, numerRej = podajDaneTegoAuta(row['IdSamochodu'], samochod_dane)
        row['Marka'] = marka
        row['Model'] = model
        row['Numer rejestracyjny'] = numerRej
    return serwis_dane

def create_extended_table_for_serwis():
    return generate_table_from_database(generate_table_from_json())
