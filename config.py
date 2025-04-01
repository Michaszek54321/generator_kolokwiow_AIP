'''
Ten moduł będzie służył do wczytywania konfiguracji z pliku config.ini oraz jej tworzenia.
'''
import configparser
import os
import pandas as pd


config = configparser.ConfigParser()


if os.name == 'nt':
    sciezka_studenci_ex = 'example\studenci.csv'
    sciezka_pytania_ex = 'example\grupy.csv'
else:
    # for mac and linux
    sciezka_studenci_ex = "example/studenci.csv"
    sciezka_pytania_ex = "example/grupy.csv"


if os.path.isfile("config.ini") == False:
    example = {
        'sciezka_studenci': 'example/studenci.csv',
        'sciezka_pytania': 'example/grupy.csv',
        'sciezka_szablonu': 'example/kolos.ipynb',
        'sciezka_docelowa': 'wygenerowane'
    }   
    config['przyklad'] = example
    with open("config.ini", 'w') as configfile:
        config.write(configfile)    

def make_config(tmp_config:dict):
    config['ostatnia_konfiguracja'] = tmp_config
    with open("config.ini", "w") as configfile:
        config.write(configfile)

config.read('config.ini')
try:
    sciezka_studenci = config['ostatnia_konfiguracja']['sciezka_studenci']
    sciezka_pytania = config['ostatnia_konfiguracja']['sciezka_pytania']
    sciezka_szablonu = config['ostatnia_konfiguracja']['sciezka_szablonu']
    sciezka_docelowa = config['ostatnia_konfiguracja']['sciezka_docelowa']
    ilosc_grup = config['ostatnia_konfiguracja']['ilosc_grup']
    tryb = config['ostatnia_konfiguracja']['tryb']
    ilosc_studentow = config['ostatnia_konfiguracja']['ilosc_studentow']
    
    ostatnia_dict = dict(config.items('ostatnia_konfiguracja'))
except KeyError:
    sciezka_studenci = ''




