'''
Ten moduł będzie służył do wczytywania konfiguracji z pliku config.ini oraz jej tworzenia.
'''
import configparser
import os
import tkinter as tk
from tkinter.filedialog import askopenfilename, askdirectory




if __name__ == "__main__":
    tk.Tk().withdraw() # część importu, jeśli nie używasz innych funkcji tkinter

    fn = askopenfilename()
    print("użytkownik wybrał", fn)

