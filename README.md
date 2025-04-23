# Projekt generator kolokwiów na Algorytmy i Programowanie

Aplikacja konsolowa do generowania kolokwiów z obsługą plików konfiguracyjnych.

Obsługa bardzo prosta. Potrzebujemy 3 pliki do operowania.
1. plik .ipynb z szablonem kolokwium. W miejscach w których chcemy zmieniające się dla studentów części wpisujemy `Zadanie tutaj`.
2. plik .csv z listą uczniów. Odzielone ; kolumny nazwane muszą być "nazwisko" dla nazwisk oraz "imie" dla imion.
3. plik .csv z częściami pytań które będzie się zmieniać. Nazwy kolumn muszą być numerem zadania (liczba naturalna).

Włączenie:
1. zainstaluj wszystkie biblioteki z pliku requierments.txt
2. wpisz komendy:
```
cd {ścieżka folderu repozytorium}
```
```
python main.py
```

Działanie:
Program pozwala na 2 opcje:
1. Automatyczne generowanie kolokwiów:
     Używając ścieżek poprzednich plików, zapisanych w konfiguracji.
2. Manualne generowanie kolokwiów:
     Manualnie wybiera się ścieżki do plików oraz wszystkie inne parametry

Samo generownaie ma 2 funkcje z grupami oraz bez grup.

Cele: 
1. tryb automatyczny ✔️
2. tryb ręcznego generowania ✔️
3. plik konfiguracyjny ✔️
3. rekomendacja ilości grup ✔️
