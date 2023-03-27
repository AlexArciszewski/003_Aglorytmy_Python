def calc_power(val:int, exp: int):
    result = 1
    
    for i in range(exp):
        result*= val
        
    return result

def calc_power(val: int, exp:int):
    if exp == 0:
        return 1
    return val*calc_power(val,exp -1)
    
def calc_fact(value:int):
    if value <= 1:
        return 1
    
    return value *calc_fact(value -1)
print(calc_fact(4)) #1*2*3*4 = 24

#odwrocona rekurencja


def calc_fact2(value: int, result: int):
    if value <=1:
        return result
    return calc_fact2(value-1,result *value)

print(calc_fact2(4,1))



#Stworzyć funkcję do której prześlę liste o rozmiarze 15 el. Funkcja na rekurencyjnie wyświetlićz wszystkie elementy z tablicy
print('z3')

from typing import Any
def print_recursive_list(arr:list[Any], index: int)-> None:
    if index == len(arr):
        return
    print(arr[index])
    
    
    return print_recursive_list(arr, index+1) 
print_recursive_list([1,2,3], 0)



#musi być wynik końcowy jako break

#wykonac sie do spełnienia warunku koncowoego


print('z3b')

from typing import Any
def print_recursive_list(arr:list[Any], index: int)-> None:
    if len(arr) == 0:
        return
    
    print(arr.pop(0))
    return print_recursive_list(arr, index + 1) 
print_recursive_list([1,2,3,4,5,6], 0 )
    
    
# Napisz program, który rekurencjnie wyświetli wszystkie liczby od N(parametr funkcji) do zera,

def n_func(number)->None:
    if number == 0:
        return
    print(number)
    return n_func(number-1)

n_func(5)



def calc_NWD(a: int, b:int):
    if b > a:
        a, b = b, a
        
    if b ==0: #skrajny warunek rekurencji
        return a
    
    return calc_NWD(b, a % b)
    # return calc_NWD(b, a-b)
    
    
    
#Zad. 2Stwórz funkcję rekurencyjnie wyliczającą, ile samogłosek ma przesłany tekst. Wynik zwróć w postaci słownika {samogłoska : ilość_wystąpień}, np.dla baadace
#freq = {‘a’ : 3, ‘e’ : 1}
print('z2')
from collections import Counter
def vowel_counter(string):
    vowels = ["a", "e", "i", "o", "u", "y"]
    dict ={}
    list=[]
    string = string.lower()
    for letter in string:
        if letter in vowels:
            list.append(letter)
    my_dict = Counter(list)
    print(my_dict)
    return my_dict
    
vowel_counter("Anakonda")





print("przyklad4")
def vowel_counter2(string):
    vowels = ["a", "e", "i", "o", "u", "y"]
    text_vowels =[]
    dict33 ={}
    string = string.lower()
    for letter in string:
        if letter in vowels:
            text_vowels.append(letter)
            print(text_vowels)
    dict33 = dict33(Counter(text_vowels))
    print(dict33)
    for key in dict33.keys():
        print(key,dict33[key])
    
    
vowel_counter("Anakonda")
from collections import Counter
def vowel_counter(string):
    vowels = ["a", "e", "i", "o", "u", "y"]
    text_vowels =[]
    dict33 ={}
    string = string.lower()
    for letter in string:
        if letter in vowels:
            text_vowels.append(letter)
    print(text_vowels)
    
    dict34 = dict(Counter(text_vowels))
    print(f"wynik to:{dict34}")
    
    for key in dict34.keys():
        print(key,dict34[key])
    return dict34
    
vowel_counter("Anakonda")

print("zad")
def vowel_counter(string):
    
    vowels = ["a", "e", "i", "o", "u", "y"]
    for letter in string:
        if letter not in vowels:
            return
    print(vowel_counter(dict(Counter(string))))

vowel_counter("baadace")


def vowel_counter(string):
    
    vowels = ["a", "e", "i", "o", "u", "y"]
    for letter in string:
        if letter in vowels:
            return print(letter)
         
    dict66 = vowel_counter(dict(Counter(string)))
    return dict66

vowel_counter("ba")

print("rekurencja zad3")

def vowel_counter(string):
    
    vowels = ["a", "e", "i", "o", "u", "y"]
    for letter in string:
        if letter in vowels:
            return print(letter)
         
    dict66 = vowel_counter(dict(Counter(string)))
    return dict66

vowel_counter("anaconda")

""" 
Spróbuj napisać rekurencję, która spowoduje crash programu w wyniku 
osiągnięcia, tzw. maksymalnej głębi przeszukiwania rekurencyjnego. 


"""

def kill_stack(n):
    if n < 1:              
        return 
        
    return kill_stack(n-1)
        
    
    
kill_stack(1000)
            
            
            
def kill_stack(n,summary):
    if n < 1:              
        return summary
    else:
        return kill_stack(n-1, sum + n)
        
    
    
kill_stack(1000,0)

""" 

import sys
print(sys.getrecursionlimit())

"""
