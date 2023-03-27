""" 
Algorytmy i struktury danych teoria Devs Mentoring
"""


""" 
Przykład 1. Algorytm wyznaczania dzielników dowolnej liczby N. Złożoność O(n) 
"""


def calc_dividers(N:int) ->list:
    dividers = []
    
    for i in range(1, N+1):
        if not N % i:  #to samo co N % i == 0 inny zapis zwyczajnie bardziej pro
            dividers.append(i)
            
    return dividers

print(calc_dividers(10)) #wyswietli 1,2,5,10 # posortowana lista

""" 
Przykład 1b. Algorytm wyznaczania dzielników dowolnej liczby N. Złożoność O(√N) 
"""


from math import sqrt

def calc_dividers(N: int) -> list:
    dividers = []
    for i in range(1, int(sqrt(N)) +1):
        if not N % i:  #to samo co N % i == 0 inny zapis zwyczajnie bardziej pro
            dividers.append(i)  #małe dzielniki
            dividers.append(N//i) #dodaj duży dzielnik
            
    return dividers
print(calc_dividers(10)) #wyswietli 1,10,2,5, nieposortowana lista aby posortowac sorted(list). 
    
    
    
    
""" 
Przykład 2. Sprawdzanie liczb pierwszych ??????Złożoność O(√N) 
"""
    
from math import *

def check_if_prime(N:int) -> bool:
    if N == 1: #wyjątek 1 nie ejst liczba pierwsza
        return False
    
    for i in range(2, int(sqrt(N) + 1)):
        if not N % i:#to samo co N % i == 0 inny zapis zwyczajnie bardziej pro
            return False #liczba nie jest pierwsza bo nie ma reszty z dzielenia 
        
    return True #for zakonczony, liczba pierwsza


print(check_if_prime(9))
print(check_if_prime(5))

""" 
Złożonośc O(N * log2log2N).

"""



def eratosthenes_sieve(N:int)->set:
    primes = set([]) #zbiór z którego będziemy wykreślać wartości
    
    for i in range(2, N + 1):
        primes.update({i}) #liczby z przedziału dodajemy do seta primes
        
    for i in range(2, N + 1):
        if i in primes: #sprawdzamy czy nie wykreslislismy
            for j in range(2 * i, N + 1, i): #jeśli nie wykreślilismy
                primes.discard(j) #to wykreślamy wszystkie wielokrotnosci liczby i
    return primes       #zwracamy zbiór z liczbami pierwszymi...

print(eratosthenes_sieve(50))        