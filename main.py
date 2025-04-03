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
    tmp_config = {}

    clear()
    print()
    print("Generator kolokwiów!\n")
    print("Mój program generuje kolokwia. Potrzebuje do tego 3 pliki.")
    print("1. Plik z szablonem kolokwium. \nTo plik .ipynb który w miejscach które mają się zmieniać dla grup/studentów ma napisane:\n `Zadanie tutaj`\n")
    print("2. Plik z rodzajami zadań. \nNa każde miejsce `Zadanie tutaj` przypadać powinno przynajmniej 1 zadanie.\n Przykładowo:")
    print(pd.read_csv(config.sciezka_pytania_ex, sep=';'))
    print()
    print("3. Plik z studentami dla których będziemy generować kolokwia.\nNajważniejsze żeby kolumny z imionami i nazwiskami \nmiały odpowiedio nazwy `imie` i `nazwisko`\n\nPrzykładowo:")
    print(pd.read_csv(config.sciezka_studenci_ex, sep=';'))
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
            tmp_config['sciezka_szablonu'] = sciezka_szablonu
            tmp_config['sciezka_pytania'] = sciezka_pytania
            tmp_config['sciezka_studenci'] = sciezka_studenci
            tmp_config['sciezka_docelowa'] = sciezka_docelowa

            print("Wybierz tryb")
            print("'bez' - tryb bez grup")
            print("'grupy' - tryb z grupami")
            nested_choice = ""
            while nested_choice=="":
                nested_choice = input("").upper()
            if nested_choice == "BEZ":
                studenci = gen.losowanie("BEZ", 0, sciezka_studenci, sciezka_pytania)
                ilosc_grup = 0
                tmp_config["tryb"] = nested_choice
            else:
                print("Wpisz ilość grup: ")
                print(f"Zalecana ilosc grup to {gen.recom_group_count(sciezka_studenci)}")
                ilosc_grup = input("")
                studenci = gen.losowanie("grupy", ilosc_grup, sciezka_studenci, sciezka_pytania)
                tmp_config["tryb"] = "GRUPY"
            
            if ilosc_grup==0:
                tmp_config["ilosc_grup"] = "rekomendowana"
            else:
                tmp_config["ilosc_grup"] = ilosc_grup

            print("Czy wygenerować kolokwia dla wszystkich studentów na liście? (Y/N)")
            nested_choice = ""
            while nested_choice=="":
                nested_choice = input("")
            if nested_choice == "Y" or nested_choice =="y":
                ilosc_studentow = 0
                gen.generator(studenci, 0, sciezka_szablonu, sciezka_docelowa)
            else:
                ilosc_studentow = input("Podaj ilość: ")
                gen.generator(studenci, ilosc_studentow, sciezka_szablonu, sciezka_docelowa)
            
            if ilosc_studentow == 0:
                tmp_config["ilosc_studentow"] = "wszyscy"
            else:
                tmp_config["ilosc_studentow"] = ilosc_studentow

            print("Gotowe!")
            print("Wpisz cokolwiek aby wrócić do menu głównego.")
            input("")

            config.make_config(tmp_config)
            
            main()

        case "2":
            clear()
            print("Automatyczne generowanie kolokwiów")
            print("")
            print("Automatyczne generowanie kolokwiów, pobiera ścieżki i opcje z poprzedniej konfiguracji.")
            print()
            if config.sciezka_studenci == '':
                print("Brak poprzedniej konfiguracji w pamięci :(")
                print("Wpisz cokolwiek aby wrócić do menu głównego.")
                input("")
                main()
            else:
                print("Ostatnia konfiguracja zawierała: ")
                print(pd.DataFrame.from_dict(config.ostatnia_dict, orient='index'))
                print("Czy chcesz kontunuować? (Y/N)")
                nested_choice = ""
                while nested_choice=="":
                    nested_choice = input("")
                if nested_choice == "Y" or nested_choice =="y":
                    print("Wpisz ilość grup: ")
                    print(f"Ostatnia ilość grup to: {config.ilosc_grup}")
                    ilosc_grup = input("")
                    studenci = gen.losowanie(config.tryb, ilosc_grup, config.sciezka_studenci, config.sciezka_pytania)

                    print("Wpisz ilość studentów: ")
                    print(f"Ostatnia ilość grup to: {config.ilosc_studentow}")
                    ilosc_studentow = input("")
                    gen.generator(studenci, ilosc_studentow, config.sciezka_szablonu, config.sciezka_docelowa)

                    print("Gotowe!")
                    print("Wpisz cokolwiek aby wrócić do menu głównego.")
                    input("")
                    main()
                else:
                    print("Wpisz cokolwiek aby wrócić do menu głównego.")
                    input("")
                    main()
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
    print("Wybierz ścieżkę do szablonu kolokwium.")
    while sciezka_szablonu == '':
        time.sleep(1)
        sciezka_szablonu = askopenfilename(filetypes=[("Jupyter Notebook","*.ipynb")], title="Wybierz szablon kolokwim")
        print(sciezka_szablonu)
        print()

    print("Wybierz ścieżkę do pliku z pytaniami (.csv)")
    while sciezka_pytania == '':
        time.sleep(1)
        sciezka_pytania = askopenfilename(filetypes=[("CSV file","*.csv")], title="Wybierz plik z pytaniami")
        print(sciezka_pytania)
        print()

    print("Wybierz ścieżkę do pliku ze studentami (.csv)")
    while sciezka_studenci == '':
        time.sleep(1)
        sciezka_studenci = askopenfilename(filetypes=[("CSV file","*.csv")], title="Wybierz plik ze studentami")
        print(sciezka_studenci)
        print()

    print("Wybierz folder docelowy wygenerowanych kolokwiów")
    while sciezka_docelowa == '':
        time.sleep(1)
        sciezka_docelowa = askdirectory(title="Wybierz plik ze studentami")
        print(sciezka_docelowa)
        print()

    klucze_pytan = pd.read_csv(sciezka_pytania, sep=';').keys()

    if '1' in klucze_pytan:
        print("Plik z pytaniami jest OK")
        print()
    else:
        print("Kolumny muszą nazywać się numerem zadania")
        print("Wybierz plik z poprawną składnią")
        return zbieranie_danych()

    if 'imie' and 'nazwisko' in pd.read_csv(sciezka_studenci, sep=';').keys():
        print("Plik z studentami jest OK")
        print()
    else:
        print("Kolumny muszą nazywać się imie i nazwisko")
        print("Wybierz plik z poprawną składnią")
        return zbieranie_danych()
    
    with open(sciezka_szablonu, "r") as szablon:
        ilosc_miejsc = szablon.read().count("Zadanie tutaj")
        if ilosc_miejsc != len(klucze_pytan):
            print("W tym szablonie nie ma wystarczającej ilości miejsc w które wchodzą pytania")
            print(f"Ilosc miejsc 'Zadanie tutaj': {ilosc_miejsc}")
            print(f"Ilosc zadań przekazanych: {len(klucze_pytan)}")
            print("Wybierz plik z poprawną składnią")
            print()
            return zbieranie_danych()

    print("Czy chcesz powtórzyć? (Y/N)")
    nested_choice = input("")
    if nested_choice == "Y" or nested_choice =="y":
        return zbieranie_danych()
    else:
        return sciezka_szablonu, sciezka_pytania, sciezka_studenci, sciezka_docelowa


if __name__ == "__main__":
    main()