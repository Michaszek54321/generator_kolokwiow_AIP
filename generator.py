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


def losowanie_bez_grup(ilosc_studentow:int = 0,
                       sciezka_studenci:str = config.sciezka_studenci, 
                       sciezka_pytania:str = config.sciezka_pytania) -> dict:
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

    if isinstance(ilosc_studentow, int) == False or ilosc_studentow == 0:
        ilosc_studentow = len(studenci)

    wylosowane_pytania = {}
    for index, row in studenci.iterrows():
        # Losowanie pytań dla każdego ucznia
        wylosowane_pytania[row['imie'] + " " + row['nazwisko']] = [random.choice(pytania[i]) for i in pytania.columns]

        if index == ilosc_studentow-1: break
    

    return wylosowane_pytania

def losowanie_z_grupami(ilosc_grup:int = 4, 
                        sciezka_studenci:str = config.sciezka_studenci, 
                        sciezka_pytania:str = config.sciezka_pytania) -> dict:
    '''
    Funkcja losująca pytania z grupami. Dla każdego ucznia losuje osobną grupę pytań.

    Args:
    sciezka_studenci (str): ścieżka do pliku z uczniami
    sciezka_pytania (str): ścieżka do pliku z rodzajami pytan
    
    Returns:
    dict:
        uczen: {grupa: [lista indexów pytań w pliku csv]}
    '''

    studenci = pd.read_csv(sciezka_studenci, sep=';')
    pytania = pd.read_csv(sciezka_pytania, sep=';')

    grupy = {_: [random.choice(pytania[i]) for i in pytania.columns] for _ in range(1, ilosc_grup+1)}
    wylosowane_pytania = {}
    
    print(grupy)

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
        
        
        for _, row in studenci.iterrows():
            if id_grupy == ilosc_grup:
                id_grupy = 0
            wylosowane_pytania[row['imie'] + " " + row['nazwisko']] = grupy[id_grupy]
            id_grupy+=1

        wylosowane_pytania = {: []  for }


    print(grupy)




if __name__ == "__main__":
    pytania = pd.read_csv("grupy.csv", sep=';')
    ilosc_grup = 4
    grupy = {_: [random.choice(pytania[i]) for i in pytania.columns] for _ in range(1, ilosc_grup+1)}
    print(grupy)


    # losowanie_z_grupami()