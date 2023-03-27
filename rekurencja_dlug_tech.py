"""
Zad. 3
Napisz program, który rekurencyjnie wyświetli wszystkie liczby od N (parametr funkcji) do 0.

"""

import timeit
import time

def func():
    x = [x for x in range(100_000_000_0000)]

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