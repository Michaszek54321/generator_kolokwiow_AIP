import sys
import os
import config


def main() -> None:
    '''
    Główna funkcja programu. Odopowaida za menu główne i obsługę terminala.
    '''
    print("Generator kolokwiów!")
    print("Wybierz jedną z opcji:")
    print("1. Automatyczne generowanie kolokwiów")
    print("2. Maunalne generowanie kolokwiów")
    print("e/E. Wyjście")

    wybor = input("Wybierz opcję: ")
    match wybor:
        case "1":
            print("Automatyczne generowanie kolokwiów")
        case "2":
            print("Manualne generowanie kolokwiów")
        case "e"|"E":
            print("Do widzenia!")
            sys.exit(0)
        
    


if __name__ == "__main__":
    main()