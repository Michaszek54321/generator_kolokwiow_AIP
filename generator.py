'''
Moduł `generator` będzie głównym modułem generującym kolokwia.
'''
import json
import config 
import pandas as pd
import random

def generator(studenci:dict, 
              sciezka_studenci:str = config.sciezka_studenci) -> None:
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


def losowanie(tryb:str, 
              ilosc_grup:int = 0, 
              sciezka_studenci:str = config.sciezka_studenci, 
              sciezka_pytania:str = config.sciezka_pytania) -> dict:
    '''
    Funkcja losująca pytania. 
    W zależności od trybu albo z grupami albo bez.

    Args:
    tryb (str): tryb funkcji
    ilosc_grup (int): ilość grup do losowania
    sciezka_studenci (str): ścieżka do pliku z uczniami
    sciezka_pytania (str): ścieżka do pliku z rodzajami pytan
    
    Returns:
    dict:
        uczen: [lista indexów pytań w pliku csv]
    '''

    studenci = pd.read_csv(sciezka_studenci, sep=';')
    pytania = pd.read_csv(sciezka_pytania, sep=';')

    
    wylosowane_pytania = {}
    if tryb == "bez":
        wylosowane_pytania = {row['imie'] + " " + row['nazwisko']: [random.choice(pytania[i]) for i in pytania.columns] for _, row in studenci.iterrows()}
    else:
        grupy = {_: [random.choice(pytania[i]) for i in pytania.columns] for _ in range(1, ilosc_grup+1)}
        
        id_grupy = 1
        for _, row in studenci.iterrows():
            if id_grupy > ilosc_grup:
                id_grupy = 1
            wylosowane_pytania[row['imie'] + " " + row['nazwisko']] = grupy[id_grupy]
            id_grupy+=1
    
    return wylosowane_pytania





if __name__ == "__main__":
    losowanie("grupy", 4)
