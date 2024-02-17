from src.Repozytorium.bazaDanychStrategy.enumPath import SAMOCHOD_PATH, SERWIS_PATH
from src.Repozytorium.bazaDanychStrategy.enumStatusSamochodu import ENUM_SERWIS, ENUM_DOSTEPNY
from src.Repozytorium.zarzadzanieFlotaPojazdow.abstractRepository import read_csv, save_updated_data_to_csv
from src.backend.servis.abstract.abstractCrateTable import create_table_from_database, generate_table_from_json, \
    create_extended_table_for_serwis
from src.backend.servis.abstract.abstractDodajDaneServices import add_data_from_json


def obsluga_zglos_usterke(values):
    add_data_from_json(values, SERWIS_PATH)
    zmiana_statusu(values.get('Numersamochodu'), ENUM_SERWIS)


def zmiana_statusu(car_id, STATUS):
    data = read_csv(SAMOCHOD_PATH)
    for car in data:
        if car['Id'] == car_id:
            car['StatusSamochodu'] = STATUS
            save_updated_data_to_csv(SAMOCHOD_PATH, data)  # Zapisz zaktualizowane dane do pliku
            break  # Zakończ pętlę po znalezieniu pasującego samochodu


def zapisz_dane(dane_po_usunieciu):
    save_updated_data_to_csv(SERWIS_PATH, dane_po_usunieciu)


def usuniecie_rekordu_po_id(id_samochodu):
    #usuniecie rekordu
    serwis_dane = read_csv(SERWIS_PATH)
    dane_po_usunieciu = [row for row in serwis_dane if not row['IdSamochodu'] == id_samochodu]
    zapisz_dane(dane_po_usunieciu)


def obsluga_usun_usterke(values):
    id_rekordu = values.get('NaprawionySamochod')
    zmiana_statusu(id_rekordu, ENUM_DOSTEPNY)
    usuniecie_rekordu_po_id(id_rekordu)


def dodaj_dane_do_tabeli_serwisu():
    pass


def zwroc_tabele():
    return create_extended_table_for_serwis()
