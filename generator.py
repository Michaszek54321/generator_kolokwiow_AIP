'''
Moduł `generator` jest głównym modułem generującym kolokwia.
'''
import json
import config 
import pandas as pd
import random
from sys import platform
from tqdm import tqdm
import time
from io import StringIO

def generator(studenci:dict, 
              ilosc_studentow:int = None,
              sciezka_szablonu:str = config.sciezka_szablonu,
              sciezka_docelowa:str = config.sciezka_docelowa) -> None:
    '''
    Funkcja generująca kolokwium.

    Args:
    studenci (dict): słownik z uczniami i wylosowanymi pytaniami
    sciezka_studenci (str): ścieżka do pliku z uczniami
    sciezka_pytania (str): ścieżka do pliku z rodzajami pytan


    Returns:
    None
    '''
    if ilosc_studentow == None or ilosc_studentow>len(studenci.keys()):
        ilosc_studentow = len(studenci.keys())

    #otwieranie potrzebnych plików
    file = open(sciezka_szablonu,"r")

    calosc = file.read() #otwarcie szablonu do zmiennej

    for uczen in tqdm(list(studenci.keys())[:ilosc_studentow], "Generowanie studentów: ",):
        #wykrywanie systemu i tworzenie ścieżki pliku
        time.sleep(0.01)
        if platform == "win32":
            sciezka_tmp = sciezka_docelowa+"\\"+uczen+".ipynb"
        else:
            sciezka_tmp = sciezka_docelowa+"/"+uczen+".ipynb"
        wnetrze = calosc

        with open(f"{sciezka_tmp}", "w") as kolos:
            for i in studenci[uczen]:
                wnetrze = wnetrze.replace("Zadanie tutaj", str(i), 1)
            kolos.write(wnetrze)


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
        uczen: [lista pytań z pliku csv]
    '''
    
    studenci, pytania = sprawdzanie_plikow(sciezka_studenci, sciezka_pytania)

    if ilosc_grup==0 or isinstance(ilosc_grup, int)==False:
        ilosc_grup = recom_group_count(sciezka_studenci)

    wylosowane_pytania = {}
    if tryb == "bez":
        wylosowane_pytania = {row['imie'] + "_" + row['nazwisko']: [random.choice(pytania[i]) for i in pytania.columns] for _, row in studenci.iterrows()}
    else:
        grupy = {}
        
        for i in pytania.columns:
            pula_pytan = pytania[i].dropna() #sprawdzanie czy nie jest niczym
            # zabezpieczenie przed błędem sample
            # jeśli ilosc grup jest większa niż pula pytań to pytania będą się powtarzały
            if len(pula_pytan)>ilosc_grup:
                for index, pytanie in enumerate(random.sample(sorted(pula_pytan), ilosc_grup), 1):
                    try:
                        grupy[index].append(pytanie)
                    except KeyError:
                        grupy[index] = [pytanie]
            else:
                index = 0
                for pytanie in pula_pytan:
                    if index > ilosc_grup: index=0
                    try:
                        grupy[index].append(pytanie)
                    except KeyError:
                        grupy[index] = [pytanie]
                    index+=1

        id_grupy = 1
        for _, row in studenci.iterrows():
            if id_grupy > ilosc_grup:
                id_grupy = 1
            wylosowane_pytania[row['imie'] + "_" + row['nazwisko']] = grupy[id_grupy]
            id_grupy+=1
    
    return wylosowane_pytania

def sprawdzanie_plikow(sciezka_studenci:str, 
                        sciezka_pytania:str):
    '''
    Funkcja sprawdzająca pliki.
    Przekształca backslashe w pytaniach na \\.

    Args:
    sciezka_studenci (str): ścieżka do pliku z uczniami
    sciezka_pytania (str): ścieżka do pliku z rodzajami pytan

    Returns:
    liste obrobionych pytań takich jak read_csv
    '''
    with open(sciezka_pytania, "r") as pytania:
        pytania = pytania.read()
        pytania = pytania.replace("\\\\", "\\")
        pytania = pytania.replace("\\", "\\\\")

    # studenci = pd.read_csv(sciezka_studenci, sep=';')
    pytania = pd.read_csv(StringIO(pytania), sep=';')

    studenci = pd.read_csv(sciezka_studenci, sep=';')

    return studenci, pytania

def recom_group_count(sciezka_studenci:str):
    '''Funkcja zwracająca zalecaną ilosc grup'''
    studenci = pd.read_csv(sciezka_studenci, sep=';')
    count = len(studenci["imie"])
    if count<3:
        return count
    for i in range(3, count+1):
        if count%i==0:
            return i

if __name__ == "__main__":
    # generator(losowanie("grupy", 4))
    losowanie("grupy", 4)
    # sprawdzanie_plikow()
    print(recom_group_count(config.sciezka_studenci))
