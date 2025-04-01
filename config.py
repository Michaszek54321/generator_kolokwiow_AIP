'''
Ten moduł będzie służył do wczytywania konfiguracji z pliku config.ini oraz jej tworzenia.
'''
import configparser
import os


config = configparser.ConfigParser


if os.name == 'nt':
    sciezka_studenci = 'example\studenci.csv'
    sciezka_pytania = 'example\grupy.csv'
    sciezka_szablonu = 'example\kolos.ipynb'
    sciezka_docelowa = 'wygenerowane'
else:
    # for mac and linux
    sciezka_studenci = "example/studenci.csv"
    sciezka_pytania = "example/grupy.csv"
    sciezka_szablonu = "example/kolos.ipynb"
    sciezka_docelowa = "wygenerowane"





# if os.path.isfile("config.ini") == False:
#     example = {
#         'sciezka_studenci': 'example/studenci.csv',
#         'sciezka_pytania': 'example/grupy.csv',
#         'sciezka_szablonu': 'example/kolos.ipynb',
#         'sciezka_docelowa': 'wygenerowane'
#     }   
#     config["przyklad"] = example
#     with open("config.ini", 'w') as configfile:
#         config.write(configfile) 

# config.read('config.ini')
# sciezka_studenci = config['user']['sciezka_studenci']
# sciezka_pytania = config['user']['sciezka_pytania']
# sciezka_szablonu = config['user']['sciezka_szablonu']
# sciezka_docelowa = config['user']['sciezka_docelowa']

