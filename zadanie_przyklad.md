#### **Zadanie: Największy wspólny dzielnik [25]**  

##### **Treść zadania:**  
Dane są dwie liczby całkowite **a** i **b**. Napisz program, który:  

1. **Wczyta od użytkownika dwie liczby całkowite a i b**.  
2. **Program powinien obsłużyć sytuację, gdy jedna z liczb jest równa 0, oraz poinformować o tym użytkownika.**
2. **Obliczy ich największy wspólny dzielnik (NWD) przy użyciu Algorytmu Euklidesa**.  
3. **Wypisze wynik na ekranie**.  

##### **Przykładowe dane wejściowe:**  
```
Podaj pierwszą liczbę: 48  
Podaj drugą liczbę: 18  
```

##### **Przykładowe dane wyjściowe:**  
```
NWD(48, 18) = 6
```

##### **Wymagania techniczne:**  
- Program powinien być podzielony na funkcje, np. `nwd(a, b)`.  
- Implementacja NWD powinna wykorzystywać **Algorytm Euklidesa** (wersja iteracyjna lub rekurencyjna).  
- Obsłuż sytuację, gdy użytkownik poda liczbę ujemną lub 0.  




#### **Zadanie: Zarządzanie kontami bankowymi – Programowanie obiektowe**  

##### **Treść zadania:**  
Napisz program, który symuluje działanie prostego systemu bankowego. W tym celu utwórz klasę **KontoBankowe**, która będzie zawierać:  

1. **Atrybuty:**  
   - `wlasciciel` – imię i nazwisko właściciela konta,  
   - `saldo` – aktualny stan konta (domyślnie 0).  

2. **Metody:**  
   - `wplata(kwota)` – zwiększa saldo konta o podaną kwotę.  
   - `wyplata(kwota)` – zmniejsza saldo konta o podaną kwotę (jeśli jest wystarczająca ilość środków).  
   - `wyswietl_saldo()` – wypisuje aktualne saldo konta.  

Zadanie tutaj

##### **Dodatkowe warunki dla różnych grup:**  
- **Grupa A:** Dodaj metodę `przelew(kwota, inne_konto)`, która pozwala na przelew środków między kontami.  
- **Grupa B:** Rozszerz klasę o obsługę limitu debetowego (np. maksymalne zadłużenie -500 zł).  
- **Grupa C:** Stwórz klasę **KontoOszczednosciowe** dziedziczącą po **KontoBankowe**, która ma dodatkową metodę `nalicz_odsetki(procent)`.  

##### **Przykładowe użycie klasy:**  
```python
konto1 = KontoBankowe("Jan Kowalski", 1000)
konto2 = KontoBankowe("Anna Nowak", 500)

konto1.wplata(200)
konto1.wyswietl_saldo()  # Powinno wyświetlić: Saldo konta Jana Kowalskiego: 1200 zł

konto1.wyplata(300)
konto1.wyswietl_saldo()  # Powinno wyświetlić: Saldo konta Jana Kowalskiego: 900 zł
```

##### **Przykładowe dane wyjściowe:**  
```
Saldo konta Jana Kowalskiego: 1200 zł  
Saldo konta Jana Kowalskiego: 900 zł  
```

##### **Wymagania techniczne:**  
- Użyj **klas i obiektów** do reprezentowania kont bankowych.  
- Obsłuż sytuację, gdy użytkownik próbuje wypłacić więcej, niż ma na koncie.  
- Zapewnij czytelne metody do manipulowania stanem konta.  

💡 **Wariant trudniejszy:** Dodaj funkcję zapisującą historię transakcji dla każdego konta.  

Podoba Ci się to zadanie? Może chcesz coś dopracować? 😊