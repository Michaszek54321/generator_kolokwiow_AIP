'''
Moduł `generator` będzie głównym modułem generującym kolokwia.
'''
import json
import config 
import pandas as pd
import random

def generator(studenci:dict, sciezka_studenci:str = config.sciezka_studenci) -> None:
    '''
    Funkcja generująca kolokwium.

    Args:
    sciezka_studenci (str): ścieżka do pliku z uczniami
    studenci (dict): słownik z uczniami i wylosowanymi pytaniami

    Returns:
    None
    '''
    json_data = json.load(open('kolos.ipynb'))

    print(json_data["cells"][0]["source"])


def losowanie_bez_grup(sciezka_studenci:str = config.sciezka_studenci, sciezka_pytania:str = config.sciezka_pytania) -> dict:
    '''
    Funkcja losująca pytania bez grup. Dla każdego ucznia losuje osobną grupę pytań.

    Args:
    sciezka_studenci (str): ścieżka do pliku z uczniami
    sciezka_pytania (str): ścieżka do pliku z rodzajami pytan
    
    Returns:
    dict:
        uczen: [lista indexów pytań w pliku csv]
    '''
    studenci = pd.read_csv(sciezka_studenci, sep=';')
    pytania = pd.read_csv(sciezka_pytania, sep=';')
    print(studenci['imie'])



def losowanie_z_grupami(sciezka_studenci:str = config.sciezka_studenci, sciezka_pytania:str = config.sciezka_pytania) -> dict:
    '''
    Funkcja losująca pytania z grupami. Dla każdego ucznia losuje osobną grupę pytań.

    Args:
    sciezka_studenci (str): ścieżka do pliku z uczniami
    sciezka_pytania (str): ścieżka do pliku z rodzajami pytan
    
    Returns:
    dict:
        uczen: {grupa: [lista indexów pytań w pliku csv]}
    '''

    pass

if __name__ == "__main__":
    losowanie_bez_grup('studenci.csv')