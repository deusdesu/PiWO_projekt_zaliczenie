# -*- coding: utf-8 -*-
import csv


def read_csv(PATH):
    data = []
    with open(PATH, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data


def update_csv(new_data, PATH):
    fieldnames = new_data[0].keys()
    with open(PATH, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(new_data[0])


def save_updated_data_to_csv(file_path, data):
    if not data:
        fieldnames = ['Id','IdSamochodu','Usterka']
    else:
        fieldnames = data[0].keys()
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
# read_csv()
# json_data = {'MarkaSamochodu': 'xxxxx', 'ModelSamochodu': 'Corsa', 'Kolor': 'biały', 'NumerRejestracyjny': '123', 'NumerVIN': '123', 'DataUbezpieczeniaPoczatek': '10.10.2020', 'DataUbezpieczeniaKoniec': '10.10.2050', 'Ubezpieczyciel': 'XXX', 'NrPolisy': 'xx', 'PoprzedniPrzegladTechniczny': '10.10.2020', 'NastepnyPrzegladTechniczny': '10.10.2050', 'StanWlasnosci': 'xx', 'Przebieg': 'zz', 'ObecnaLokalizacja': 'yy', 'StatusSamochodu': 'zz', 'TypPaliwa': 'zz', 'SrednieSpalanie': '5', 'SkrzyniaBiegow': 'manual', 'DystansDoPrzejechania': '1000'}
# add_car_from_json(json_data)
# read_csv()
