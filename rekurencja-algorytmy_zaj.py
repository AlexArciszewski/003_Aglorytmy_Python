"""

Stwórz funkcję rekurencyjnie wyliczającą, ile samogłosek ma przesłany tekst. Wynik zwróć w postaci słownika {samogłoska : ilość_wystąpień}, np.
dla baadace
freq = {‘a’ : 3, ‘e’ : 1}
"""

# ZLONOSC OBLICZENIOWY O(n):
# def sum_numbers(numbers): # -> 10 / 100 / 1000/ 10000
#     result = 0
#     for num in numbers:
#         result += num
#     return result
#
# # zlozonosc olibzceniowa  O(N^2)
# def find_duplicates(items):
#     duplicates = []
#     for i in range(len(items)):#  4**2 -> 16 10* 10** 2 -> 100
#         for j in range(i + 1, len(items)):
#             if items[i] == items[j] and items[i] not in duplicates:
#                 duplicates.append(items[i])
#     return duplicates
#
#
# # zloznosc obliczeniow O(1)
# def add_numbers(a, b):
#     return a+b
#
#
# from math import *
#
#
#
# def check_if_prime(N: int) -> bool:
#     if N == 1:  # wyjątek 1 nie ejst liczba pierwsza
#         return False
#
#     for i in range(2, int(sqrt(N) + 1)):
#         if not N % i:  # to samo co N % i == 0 inny zapis zwyczajnie bardziej pro
#             return False  # liczba nie jest pierwsza bo nie ma reszty z dzielenia
#
#     return True  # for zakonczony, liczba pierwsza
#
#
# print(check_if_prime(9))
# print(check_if_prime(5))



numbers = [1,2, 3, 4, 5, -1]
result = all(num> 0 for num in numbers) # -> all(true,true,true,true,true,true)

result = []
for num in numbers:
    if num > 0:
        result.append(True)
    else:
        result.append(False)
print(result)
print(all(result))
print(not all(result))

print(any(result)) # _> Nie wszystkie elementy sa true
print(not any(result)) # _-> Czy jakis element nie jest True


if result[0] and result[1] and result[2]:
    print()
    
"""
Zad. 3
Napisz program, który rekurencyjnie wyświetli wszystkie liczby od N (parametr funkcji) do 0.

"""

import timeit
import time

def func():
    x = [x for x in range(100_000_000)]

# x = timeit.timeit(func)
#

start_time = time.time()
func()
end_time = time.time()

elapsed_time = end_time - start_time
print(f"{elapsed_time:.2f}")
# print(x)



# def n_func(number: int) -> None:
#     if number == 0:
#         return
#     print(number)
#     return n_func(number - 1)
#
#
#
# n_func(15)


"""
Stwórz funkcję rekurencyjnie wyliczającą, ile samogłosek ma przesłany tekst. Wynik zwróć w postaci słownika {samogłoska : ilość_wystąpień}, np.
dla baadace
freq = {‘a’ : 3, ‘e’ : 1}
"""

# def vowel_counter(text: str, freq = None):
#     if not freq:
#         freq = {}
#     if len(text) == 0:
#         return freq
#     vowels = ["a", "e", "i", "o", "u", "y"]
#     first_char = text[0].lower()
#     if first_char not in vowels:
#         print(text)
#         return vowel_counter(text[1:], freq) # -> 'aaeeiii' -> aeeiii -> eeiii -> eiii -> iii -> ii -> i
#     else:
#         print(text)
#         freq[first_char] = freq.get(first_char, 0) + 1
#     return vowel_counter(text[1:], freq)

def vowel_counter(text: str, idx = 0, freq=None): # -> 'qujeiqwoejqwuicjmqwuchqwuchqwuiopueiasueiqwueiquweiqwueiqw'
    vowels = ["a", "e", "i", "o", "u", "y"]
    if not freq:
        freq = {}
    if idx == len(vowels):
        return freq
    no_of_letters = text.count(vowels[idx])
    if no_of_letters:
        freq[vowels[idx]] = no_of_letters
    return vowel_counter(text, idx + 1, freq)
    # for letter in string:
    #     if letter in vowels:
    #         list.append(letter)
    # my_dict = Counter(list)
    # print(my_dict)
    # return my_dict
    # .count('a')

print(vowel_counter('aaeeiii'))