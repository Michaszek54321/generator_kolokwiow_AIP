import sys
import os
import config
import pandas as pd
import tkinter as tk
from tkinter.filedialog import askopenfilename, askdirectory
import time
import generator as gen

tk.Tk().withdraw()



def clear():
    '''Funkcja czyszcząca terminal'''
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux
    else:
        _ = os.system('clear')


def main() -> None:
    '''
    Główna funkcja programu. Odopowaida za menu główne i obsługę terminala.
    '''
    sciezka_szablonu = ''
    sciezka_pytania = ''
    sciezka_studenci = ''
    sciezka_docelowa = ''
    studenci = {}
    config = {}


    print("Generator kolokwiów!\n")
    print("Mój program generuje kolokwia. Potrzebuje do tego 3 pliki.")
    print("1. Plik z szablonem kolokwium. \nTo plik .ipynb który w miejscach które mają się zmieniać dla grup/studentów ma napisane:\n `Zadanie tutaj`\n")
    print("2. Plik z rodzajami zadań. \nNa każde miejsce `Zadanie tutaj` przypadać powinno przynajmniej 1 zadanie.\n Przykładowo:")
    print(pd.read_csv(config.sciezka_pytania, sep=';'))
    print()
    print("3. Plik z studentami dla których będziemy generować kolokwia.\nNajważniejsze żeby kolumny z imionami i nazwiskami \nmiały odpowiedio nazwy `imie` i `nazwisko`\n\nPrzykładowo:")
    print(pd.read_csv(config.sciezka_studenci, sep=';'))
    print()
    print("Po wyborze jednej z opcji zdefiniujesz ścieżki do tych plików: ")
    print("1. Maunalne generowanie kolokwiów")
    print("2. Automatyczne generowanie kolokwiów")
    print("e/E. Wyjście")

    wybor = input("Wybierz opcję: ")
    clear()
    match wybor:
        case "1":
            nested_choice = ""
            clear()
            print("Manualne generowanie kolokwiów")
            print("")
            sciezka_szablonu, sciezka_pytania, sciezka_studenci, sciezka_docelowa = zbieranie_danych()
            config['sciezka_szablonu'] = sciezka_szablonu
            config['sciezka_pytania'] = sciezka_pytania
            config['sciezka_studenci'] = sciezka_studenci
            config['sciezka_docelowa'] = sciezka_docelowa

            print("Wybierz tryb")
            print("'bez' - tryb bez grup")
            print("'grupy' - tryb z grupami")
            nested_choice = ""
            while nested_choice=="":
                nested_choice = input("").upper()
            if nested_choice == "GRUPY":
                print("Wpisz ilość grup: ")
                print(f"Zalecana ilosc grup to {gen.recom_group_count(sciezka_studenci)}")
                ilosc_grup = input("")
                studenci = gen.losowanie("grupy", ilosc_grup, sciezka_studenci, sciezka_pytania)
            else:
                studenci = gen.losowanie("bez", 0, sciezka_studenci, sciezka_pytania)
                ilosc_grup = 0
            
            config["tryb"] = nested_choice
            config["ilosc_grup"] = ilosc_grup

            print("Czy wygenerować kolokwia dla wszystkich studentów na liście? (Y/N)")
            nested_choice = ""
            while nested_choice=="":
                nested_choice = input("")
            if nested_choice == "Y" or nested_choice =="y":
                ilosc = None
                gen.generator(studenci, None, sciezka_szablonu, sciezka_docelowa)
            else:
                ilosc = input("Podaj ilość: ")
                gen.generator(studenci, ilosc, sciezka_szablonu, sciezka_docelowa)
            
            config["ilosc_studentow"] = ilosc

            print("Gotowe!")
            print("Wpisz cokolwiek aby wrócić do menu głównego.")
            input("")
            main()

        case "2":
            clear()
            print("Automatyczne generowanie kolokwiów")
            print("")
            print("Automatyczne generowanie kolokwiów, pobiera ścieżki z poprzednich")
            
        case "e"|"E":
            print("Do widzenia!")
            sys.exit(0)
        case _:
            main()
    

def zbieranie_danych():
    sciezka_szablonu = ''
    sciezka_pytania = ''
    sciezka_studenci = ''
    sciezka_docelowa = ''
    print("Wybierz ścieżkę do szablonu kolokwium.\n")
    while sciezka_szablonu == '':
        time.sleep(1)
        sciezka_szablonu = askopenfilename(filetypes=[("Jupyter Notebook","*.ipynb")], title="Wybierz szablon kolokwim")
        print(sciezka_szablonu)

    print("Wybierz ścieżkę do pliku z pytaniami (.csv)\n")
    while sciezka_pytania == '':
        time.sleep(1)
        sciezka_pytania = askopenfilename(filetypes=[("CSV file","*.csv")], title="Wybierz plik z pytaniami")
        print(sciezka_pytania)

    print("Wybierz ścieżkę do pliku ze studentami (.csv)\n")
    while sciezka_studenci == '':
        time.sleep(1)
        sciezka_studenci = askopenfilename(filetypes=[("CSV file","*.csv")], title="Wybierz plik ze studentami")
        print(sciezka_studenci)

    print("Wybierz folder docelowy wygenerowanych kolokwiów\n")
    while sciezka_docelowa == '':
        time.sleep(1)
        sciezka_docelowa = askdirectory(title="Wybierz plik ze studentami")
        print(sciezka_docelowa)

    print()

    return sciezka_szablonu, sciezka_pytania, sciezka_studenci, sciezka_docelowa


if __name__ == "__main__":
    main()