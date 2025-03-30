# Projekt generator kolokwiów na Algorytmy i Programowanie

Aplikacja konsolowa do generowania kolokwiów z obsługą plików konfiguracyjnych.

Obsługa bardzo prosta. Potrzebujemy 3 pliki do operowania.
1. plik .ipynb z szablonem kolokwium. W miejscach w których chcemy zmieniające się dla studentów części wpisujemy `Zadanie tutaj`.
2. plik .csv z listą uczniów. Odzielone ; kolumny nazwane muszą być "nazwisko" dla nazwisk oraz "imie" dla imion.
3. plik .csv z częściami pytań które będzie się zmieniać. Nazwy kolumn muszą być numerem zadania (liczba naturalna).

Podczas konfiguracji można ustawić ścieżki do tych plików jak i folderu docelowego w którym będą tworzone pliki dla uczniów.
W planach również dodaie obsługi google colab.


Cele: 
1. tryb automatyczny
2. tryb ręcznego generowania
3. implementacja dysku google
4. generowanie dla listy uczniów
5. plik konfiguracyjny
