#Bubble sort
def bubble_sort(array: list):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]: #  array[j] <array[j+1] dla sort. nierosnącego
                array[j], array[j+1] = array[j+1], array[j]
                
def main():
    array =[2, 9, 5, 2, -10, -20, -4, 0, 1, 4, 3]
    bubble_sort(array)
    
    print(array)
    
if __name__ == "__main__":
    main()



   
#IndexError: list index out of range On2 malo wydajne sortowanie babelkowe




#Insertion sort O(n2)

def insertion_sort(array: list):
    for i in range(1, len(array)):
        key = array[i]
        
        j = i - 1
        while j>= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        
        array[j +1] = key
        
def main():
    array =[2, 9, 5, 2, -10, -20, -4, 0, 1, 4, 3]
    insertion_sort(array)
    
    print(array)
    
if __name__ == "__main__":
    main()

#result:[-20, -10, -4, 0, 1, 2, 2, 3, 4, 5, 9]
        
#quick sort O(n*log2N) z pivotem

#to pivot
def partition(array: list, i: int, j: int):
    pivot_idx = (i +j) //2
    pivot = array[pivot_idx]
    
    while i <= j:
        while pivot > array[i]:  # jak niemalejaco to zamień pivot < array[i]
            i += 1
        while pivot < array[j]:  # jak niemalejaco to zamień pivot > array[j]
            j -= 1
        
        if i<= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
    return i
    
#to funkcja sortująca
def quick_sort(array: list, start: int, end: int):
    edge = partition(array = array, i = start, j = end)
    
    if start < edge -1:
        quick_sort(array=array, start = start, end = edge -1)
    
    if end > edge:
        quick_sort(array = array , start = edge, end = end)

#funkcja główna

def main():
    array = [2, 9, 5, 2, -10, -20, -4, 0, 1, 4, 3]
    
    quick_sort(array=array, start=0, end=len(array) -1)
    print(array)

if __name__ == "__main__":
    main()
""" 
Zad. 1
Stwórz program, który zbada czas sortowania poznanymi metodami (Bubble Sort, Insertion Sort, Quick Sort) list o elementach
1000, 10 000, 100 000, 1 000 000 elementów. Wyniki zapisz do pliku tekstowego. Listę wypełniaj losowymi wartościami przy 
wykorzystaniu modułu random, a czas mierz przy użyciu time.

Podpowiedź:
Pomiar czasu wykonania:

>>> import datetime 
>>> a = datetime.datetime.now() 
>>> b = datetime.datetime.now() 
>>> c = b - a 
>>> c 
datetime.timedelta(0, 4, 316543) 
>>> c.days 
0 
>>> c.seconds 
4 
>>> c.microseconds 
316543

"""
import datetime
import random

#list generators

random_1000 = []
for _ in range(1,1001):
    n = random.randint(1,1001)
    random_1000.append(n)
print(random_1000)


random_10000 =[]
for _ in range(1,10001):
    m =random.randint(1, 10001)
    random_10000.append(m)
print(random_10000)

random_100000 =[]
for _ in range(1,100001):
    o =random.randint(1, 100001)
    random_100000.append(o)
print(random_100000)

random_1000000 =[]
for _ in range(1,1000001):
    o =random.randint(1, 1000001)
    random_1000000.append(o)
print(random_1000000)
#bubble sort
def bubble_sort(array: list):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]: #  array[j] <array[j+1] dla sort. nierosnącego
                array[j], array[j+1] = array[j+1], array[j]
                
                
def insertion_sort(array: list):
    for i in range(1, len(array)):
        key = array[i]
        
        j = i - 1
        while j>= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        
        array[j +1] = key

#quick sort O(n*log2N) z pivotem

#pivot

def partition(array: list, i: int, j: int):
    pivot_idx = (i +j) //2
    pivot = array[pivot_idx]
    
    while i <= j:
        while pivot > array[i]:  # jak niemalejaco to zamień pivot < array[i]
            i += 1
        while pivot < array[j]:  # jak niemalejaco to zamień pivot > array[j]
            j -= 1
        
        if i<= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
    return i


#sorting function
def quick_sort(array: list, start: int, end: int):
    edge = partition(array = array, i = start, j = end)
    
    if start < edge -1:
        quick_sort(array=array, start = start, end = edge -1)
    
    if end > edge:
        quick_sort(array = array , start = edge, end = end)










             
def main():
#bubble-sort
    
    a = datetime.datetime.now() 
    bubble_sort(random_1000)
    b = datetime.datetime.now() 
    c = b - a 
    print(f"bubble sort 1000 elements {random_1000}")
    print(c)
    d =str(c)
    
    
    a1 = datetime.datetime.now() 
    bubble_sort(random_10000)
    b1 = datetime.datetime.now() 
    c1 = b1 - a1 
    print(f"bubble sort 1000 elements {random_10000}")
    print(c1)
    d1 =str(c1)
    
    
    a2 = datetime.datetime.now() 
    bubble_sort(random_100000)
    b2 = datetime.datetime.now() 
    c2 = b2 - a2 
    print(f"bubble sort 1000 elements {random_100000}")
    print(c2)
    d2 =str(c2)
    
    a3 = datetime.datetime.now() 
    bubble_sort(random_1000000)
    b3 = datetime.datetime.now() 
    c3 = b3 - a3 
    print(f"bubble sort 1000 elements {random_1000000}")
    print(c3)
    d3 =str(c3)
    
    
    #insertion sort
    
    
    a4 = datetime.datetime.now() 
    insertion_sort(random_1000)
    b4 = datetime.datetime.now()
    c4 = b4 - a4 
    print(f"insertion sort 1000 elements {random_1000}")
    print(c4)
    d4 =str(c4)


    a5 = datetime.datetime.now() 
    insertion_sort(random_10000)
    b5 = datetime.datetime.now()
    c5 = b5 - a5 
    print(f"insertion sort 10000 elements {random_10000}")
    print(c5)
    d5 =str(c5)
    
    
    a6 = datetime.datetime.now() 
    insertion_sort(random_100000)
    b6 = datetime.datetime.now()
    c6 = b6 - a6 
    print(f"insertion sort 100000 elements {random_100000}")
    print(c6)
    d6 =str(c6)
    
    
    a7 = datetime.datetime.now() 
    insertion_sort(random_1000000)
    b7 = datetime.datetime.now()
    c7 = b7 - a7 
    print(f"insertion sort 1000000 elements {random_1000000}")
    print(c7)
    d7 =str(c7)
    
    
    
    
    
    #quick_sort(array=array, start=0, end=len(array) -1)
    #print(array)
    
    
    a8 = datetime.datetime.now()
    quick_sort(random_1000, start=1,end =len(random_1000)-1)
    b8 = datetime.datetime.now()
    c8 = b8 - a8 
    print(f" quick sort 1000 elements {random_1000}")
    print(c8)
    d8 =str(c8)
    
    a9 = datetime.datetime.now()
    quick_sort(random_10000, start=1,end =len(random_10000)-1)
    b9 = datetime.datetime.now()
    c9 = b9 - a9 
    print(f" quick sort 10000 elements {random_10000}")
    print(c9)
    d9 =str(c9)
    
    a10 = datetime.datetime.now()
    quick_sort(random_100000, start=1,end =len(random_100000)-1)
    b10 = datetime.datetime.now()
    c10 = b10 - a10 
    print(f" quick sort 100000 elements {random_100000}")
    print(c10)
    d10 =str(c10)
    
    a11 = datetime.datetime.now()
    quick_sort(random_1000000, start=1,end =len(random_1000000)-1)
    b11 = datetime.datetime.now()
    c11 = b11 - a11 
    print(f" quick sort 1000000 elements {random_1000000}")
    print(c11)
    d11 =str(c11)
    
    
    
    #SHORT-VERSION
    lines = ['Sorted_readme','The times for bubble sorting are:',d,  'The times for insertion sorting are:', d4, 'The times for quick sorting are:', d8]
    #lines = ['Sorted_readme','The times for bubble sorting are:',d , d1, d2, d3 , 'The times for insertion sorting are:', d4, d5, d6, d7, 'The times for quick sorting are:', d8, d9,d10,d11 ]
    with open("sorted_readme.txt","w") as f:
        for line in lines:
            f.write(line)
            f.write('\n')
        
if __name__ == "__main__":
    main()