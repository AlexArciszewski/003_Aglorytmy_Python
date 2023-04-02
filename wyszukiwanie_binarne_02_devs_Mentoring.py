"""
Zad 2.
Mając dane liczby naturalne p i q, znajdź taką liczbę naturalną x, dla której
x3 + px = q
lub ustal, że taka liczba nie istnieje
Wejście
W pierwszym wierszu wejścia znajduje się liczba zagadek z, nie większa niż 10 000. W kolejnych wierszach podajesz liczby naturalne p i q. Obie liczby są dodatnie, liczba p nie przekracza 1012, zaś q – 1018. Liczby są oddzielone pojedynczym odstępem, każda zagadka podana jest w osobnym wierszu.
Wyjście
Wypisz odpowiedzi na wszystkie zagadki, w tej kolejności, w jakiej były podane na wejściu. Odpowiedź powinna być liczbą naturalną spełniającą podane równanie. Jeśli taka liczba nie istnieje, zamiast liczby wypisz słowo NIE.
Przykład
Dla danych wejściowych:
2
3 14
7 10
poprawnym wynikiem jest:
2
NIE


"""

from memory_profiler import profile
#
# q = 2
# f = x ** 3 + p * x
# if f == q:
#     pass

@profile
def find_x(p: int, q: int) -> str:
    end = int(q ** (1/3)) + 1
    for x in range(q):
        if x ** 3 + p * x == q:
            return str(x)
    return "NIE"


@profile
def find_x_binary(p: int, q: int) -> str:
    left = 0
    right = q#int(q ** (1/3)) + 1

    while left <= right:
        mid = (left + right) // 2
        f = mid ** 3 + p * mid
        if f == q:
            return str(mid)
        elif f < q:
            left = mid + 1
        else:
            right = mid - 1

    return "NIE"

def main() -> None:
    n = int(input("Podaj ilosc zaggadek"))
    for _ in range(n):
        p, q = map(int, input().split())
        print(find_x(p, q))
        print(find_x_binary(p, q))

if __name__ == "__main__":
    main()