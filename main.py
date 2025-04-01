import sys
import os
import config
import pandas as pd
import tkinter as tk
from tkinter.filedialog import askopenfilename, askdirectory
import time
import generator as gen
import keyboard

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

            studenci = gen.losowanie("grupy", 4, sciezka_studenci, sciezka_pytania)

            print("Czy wygenerować kolokwia dla wszystkich studentów na liście? (Y/N)")
            while nested_choice=="":
                nested_choice = input("")
            if nested_choice == "Y" or nested_choice =="y":
                gen.generator(studenci, None, sciezka_szablonu, sciezka_docelowa)
            else:
                ilosc = input("Podaj ilość: ")
                gen.generator(studenci, ilosc, sciezka_szablonu, sciezka_docelowa)

            print("Gotowe!")
            print("Kliknij Enter aby wrócić do menu głównego.")
            if keyboard.is_pressed('enter'):
                main()



        case "2":
            print("Automatyczne generowanie kolokwiów")
            automatyczne()
            
        case "e"|"E":
            print("Do widzenia!")
            sys.exit(0)
        case _:
            main()
    

def manualne(sciezka_studenci):
    clear()
    print("Manualne generowanie kolokwiów")
    print("")
    zbieranie_danych()

    studenci = gen.losowanie("grupy", 4, sciezka_studenci, )

    

    pass

def automatyczne():
    pass

def zbieranie_danych():
    sciezka_szablonu = ''
    sciezka_pytania = ''
    sciezka_studenci = ''
    sciezka_docelowa = ''
    print("Podaj ścieżkę do szablonu kolokwium.\n")
    while sciezka_szablonu == '':
        time.sleep(0.5)
        sciezka_szablonu = askopenfilename(filetypes=[("Jupyter Notebook","*.ipynb")], title="Wybierz szablon kolokwim")

    print("Podaj ścieżkę do pliku z pytaniami (.csv)\n")
    while sciezka_pytania == '':
        time.sleep(0.5)
        sciezka_pytania = askopenfilename(filetypes=[("CSV file","*.csv")], title="Wybierz plik z pytaniami")

    print("Podaj ścieżkę do pliku ze studentami (.csv)\n")
    while sciezka_studenci == '':
        time.sleep(0.5)
        sciezka_studenci = askopenfilename(filetypes=[("CSV file","*.csv")], title="Wybierz plik ze studentami")

    print("Podaj folder docelową wygenerowanych kolokwiów\n")
    while sciezka_docelowa == '':
        time.sleep(0.5)
        sciezka_docelowa = askdirectory(title="Wybierz plik ze studentami")

    print()

    return sciezka_szablonu, sciezka_pytania, sciezka_studenci, sciezka_docelowa


if __name__ == "__main__":
    main()