import json

from Repozytorium.samochod.samochod import read_csv, update_csv


def add_car_from_json(json_data):
    data = read_csv()
    car_data = dodajId(data, json_data)
    update_csv([car_data])


def dodajId(data, json_data):
    new_car_id = len(data) + 1
    json_data['Id'] = str(new_car_id)
    json_str = json.dumps(json_data)
    car_data = json.loads(json_str)
    car_data = {'Id': car_data['Id'], **car_data}  # Przesunięcie 'Id' na początek
    return car_data
