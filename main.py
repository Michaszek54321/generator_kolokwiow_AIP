import sys
import os
import config
import pandas as pd

def main() -> None:
    '''
    Główna funkcja programu. Odopowaida za menu główne i obsługę terminala.
    '''
    print("Generator kolokwiów!")
    print("Mój program generuje kolokwia. Potrzebuje do tego 3 pliki.")
    print("1. Plik z szablonem kolokwium. To plik .ipynb który w miejscach które mają się zmieniać dla grup/studentów ma napisane:\n Zadanie tutaj\n")
    print("2. Plik z rodzajami zadań, ")
    print("Wybierz jedną z opcji:")
    print("1. Maunalne generowanie kolokwiów")
    print("2. Automatyczne generowanie kolokwiów")
    print("e/E. Wyjście")

    wybor = input("Wybierz opcję: ")
    sys.clear()
    match wybor:
        case "1":
            print("Manualne generowanie kolokwiów")

        case "2":
            print("Automatyczne generowanie kolokwiów")
            
        case "e"|"E":
            print("Do widzenia!")
            sys.exit(0)
    

def manualne():
    print("### Manualne generowanie kolokwiów ###")
    print("")
    print("Podaj ścieżkę do ")
    pass

def automatyczne():
    pass

if __name__ == "__main__":
    main()