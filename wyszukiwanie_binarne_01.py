"""
Zad 1.
Wygeneruj listę 30 elementów składających się z liczb całkowitych z przedziału [0, 30]. Następnie, wykorzystując
wyszukiwanie binarne, sprawdź, czy znajduje się w niej co najmniej 10 liczb większych od wartości 20. Pamiętaj o
odpowiednim zmodyfikowaniu listy, aby możliwe było przeprowadzenie procesu wyszukiwania binarnego.w
"""
from random import randint

def random_list() -> list[int]:
    arr = []
    for i in range(30):
        arr.append(randint(0,30))
    arr.sort(reverse=False)
    return arr

def binary(arr: list[int], number:int) -> bool:
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == number:
            return True
        if arr[mid] < 20:
            left = mid + 1
        elif arr[mid] > 20:
            right = mid - 1
    return False




arr = random_list()
result = binary(arr, 20)
if result:
    print(arr)
    x = arr.index(20)
    if len(arr) - x > 10:
        print("Tak")
else:
    print("Nie ma liczby 20")



"""
def number_gen(values):
    arr = []
    for idx in range(0, values):
        arr.append(idx)
    print(arr)
    score = 0
    for number in arr:
        if number > 20:
            score += 1
    if score >= 10:
        return True


print(number_gen(31))


def bin_search(number: int):
    left = 0
    list = []
    list2 = []
    score = 0
    while left <= right:
        mid = (left + right) // 2

        if list[mid] < 20:
            left = mid + 1

        elif list[mid] > 20:
            right = mid - 1
            # score += 1
        else:
            return (mid)

        print(mid)


print(bin_search(30))
"""


def bin_search(number: int):
    left = 0
    list = []
    list2 = []
    score = 0
    for i in range(0, number):
        list.append(i)
    right = len(list)
    # print(right)

