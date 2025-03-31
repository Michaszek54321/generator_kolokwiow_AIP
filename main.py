import sys
import os
import config
import pandas as pd
import tkinter as tk
from tkinter.filedialog import askopenfilename, askdirectory


def clear():
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
    print("Generator kolokwiów!E\n")
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
            print("Manualne generowanie kolokwiów")
            manualne()

        case "2":
            print("Automatyczne generowanie kolokwiów")
            automatyczne()
            
        case "e"|"E":
            print("Do widzenia!")
            sys.exit(0)
    

def manualne():
    print("Manualne generowanie kolokwiów")
    print("")
    print("Podaj ścieżkę do szablonu kolokwium.")
    tk.Tk().withdraw() # część importu, jeśli nie używasz innych funkcji tkinter
    fn = askopenfilename()
    print("użytkownik wybrał", fn)
    pass

def automatyczne():
    pass

if __name__ == "__main__":
    main()