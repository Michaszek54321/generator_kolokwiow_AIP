'''
Moduł `generator` będzie głównym modułem generującym kolokwia.
'''
import json
import config 
import csv
import random

json_data = json.load(open('kolos.ipynb'))

print(json_data["cells"][0]["source"])

def losowanie_bez_grup(sciezka_uczniowie:str = config.sciezka_uczniowie, sciezka_pytania:str = config.sciezka_pytania) -> dict:
    '''
    Funkcja losująca pytania bez grup. Dla każdego ucznia losuje osobną grupę pytań.

    Args:
    sciezka_uczniowie (str): ścieżka do pliku z uczniami
    sciezka_pytania (str): ścieżka do pliku z rodzajami pytan
    
    Returns:
    dict:
        uczen: [lista indexów pytań w pliku csv]
    '''
    
    pass


def losowanie_z_grupami(sciezka_uczniowie:str = config.sciezka_uczniowie, sciezka_pytania:str = config.sciezka_pytania) -> dict:
    '''
    Funkcja losująca pytania z grupami. Dla każdego ucznia losuje osobną grupę pytań.

    Args:
    sciezka_uczniowie (str): ścieżka do pliku z uczniami
    sciezka_pytania (str): ścieżka do pliku z rodzajami pytan
    
    Returns:
    dict:
        uczen: {grupa: [lista indexów pytań w pliku csv]}
    '''

    pass
    