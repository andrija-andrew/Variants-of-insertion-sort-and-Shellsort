import math

RHO_PLUS_1 = 2.324717957244746    # plastic constant + 1


def Shellsort0(lst: list):
    n = len(lst)
    d = n >> 1
    while d:
        for i in range(n - d):
            if lst[i] > lst[i + d]:
                lst[i + d], lst[i] = lst[i], lst[i + d]
                for j in range(i, d - 1, -d):
                    if lst[j - d] > lst[j]:
                        lst[j], lst[j - d] = lst[j - d], lst[j]
                    else:
                        break
        d >>= 1


def inverted_Shellsort0(lst: list):
    n = len(lst)
    d = n >> 1
    while d:
        for i in range(n - 1, d - 1, -1):
            if lst[i - d] > lst[i]:
                lst[i], lst[i - d] = lst[i - d], lst[i]
                for j in range(i + d, n, d):
                    if lst[j - d] > lst[j]:
                        lst[j], lst[j - d] = lst[j - d], lst[j]
                    else:
                        break
        d >>= 1


def Shellsort1(lst: list):
    n = len(lst)
    d = (1 << (n >> 1).bit_length()) - 1
    while d:
        for i in range(n - d):
            if lst[i] > lst[i + d]:
                lst[i + d], lst[i] = lst[i], lst[i + d]
                for j in range(i, d - 1, -d):
                    if lst[j - d] > lst[j]:
                        lst[j], lst[j - d] = lst[j - d], lst[j]
                    else:
                        break
        d >>= 1


def inverted_Shellsort1(lst: list):
    n = len(lst)
    d = (1 << (n >> 1).bit_length()) - 1
    while d:
        for i in range(n - 1, d - 1, -1):
            if lst[i - d] > lst[i]:
                lst[i], lst[i - d] = lst[i - d], lst[i]
                for j in range(i + d, n, d):
                    if lst[j - d] > lst[j]:
                        lst[j], lst[j - d] = lst[j - d], lst[j]
                    else:
                        break
        d >>= 1


def Shellsort2(lst: list):
    n = len(lst)
    d = int(n // RHO_PLUS_1)
    while d > 2:
        for i in range(n - d):
            if lst[i] > lst[i + d]:
                lst[i + d], lst[i] = lst[i], lst[i + d]
                for j in range(i, d - 1, -d):
                    if lst[j - d] > lst[j]:
                        lst[j], lst[j - d] = lst[j - d], lst[j]
                    else:
                        break
        d = int(d // RHO_PLUS_1)

    for i in range(n - 1):
        if lst[i] > lst[i + 1]:
            lst[i + 1], lst[i] = lst[i], lst[i + 1]
            for j in range(i, 0, -1):
                if lst[j - 1] > lst[j]:
                    lst[j], lst[j - 1] = lst[j - 1], lst[j]
                else:
                    break


def inverted_Shellsort2(lst: list):
    n = len(lst)
    d = int(n // RHO_PLUS_1)
    while d > 2:
        for i in range(n - 1, d - 1, -1):
            if lst[i - d] > lst[i]:
                lst[i], lst[i - d] = lst[i - d], lst[i]
                for j in range(i + d, n, d):
                    if lst[j - d] > lst[j]:
                        lst[j], lst[j - d] = lst[j - d], lst[j]
                    else:
                        break
        d = int(d // RHO_PLUS_1)

    for i in range(n - 1, 0, -1):
        if lst[i - 1] > lst[i]:
            lst[i], lst[i - 1] = lst[i - 1], lst[i]
            for j in range(i + 1, n):
                if lst[j - 1] > lst[j]:
                    lst[j], lst[j - 1] = lst[j - 1], lst[j]
                else:
                    break


def Shellsort3(lst: list):
    n = len(lst)
    if n > 1:
        d = (1 << ((n >> 1) - 1).bit_length()) | 1
        while True:
            for i in range(n - d):
                if lst[i] > lst[i + d]:
                    lst[i + d], lst[i] = lst[i], lst[i + d]
                    for j in range(i, d - 1, -d):
                        if lst[j - d] > lst[j]:
                            lst[j], lst[j - d] = lst[j - d], lst[j]
                        else:
                            break
            if d > 1:
                d = (d >> 1) | 1
            else:
                return


def inverted_Shellsort3(lst: list):
    n = len(lst)
    if n > 1:
        d = (1 << ((n >> 1) - 1).bit_length()) | 1
        while True:
            for i in range(n - 1, d - 1, -1):
                if lst[i - d] > lst[i]:
                    lst[i], lst[i - d] = lst[i - d], lst[i]
                    for j in range(i + d, n, d):
                        if lst[j - d] > lst[j]:
                            lst[j], lst[j - d] = lst[j - d], lst[j]
                        else:
                            break
            if d > 1:
                d = (d >> 1) | 1
            else:
                return


def Shellsort4(lst: list):
    n = len(lst)
    for k in range(int(math.log(n, 3)) if n > 8 else 1, 0, -1):
        d = (3 ** k - 1) >> 1
        for i in range(n - d):
            if lst[i] > lst[i + d]:
                lst[i + d], lst[i] = lst[i], lst[i + d]
                for j in range(i, d - 1, -d):
                    if lst[j - d] > lst[j]:
                        lst[j], lst[j - d] = lst[j - d], lst[j]
                    else:
                        break


def inverted_Shellsort4(lst: list):
    n = len(lst)
    for k in range(int(math.log(n, 3)) if n > 8 else 1, 0, -1):
        d = (3 ** k - 1) >> 1
        for i in range(n - 1, d - 1, -1):
            if lst[i - d] > lst[i]:
                lst[i], lst[i - d] = lst[i - d], lst[i]
                for j in range(i + d, n, d):
                    if lst[j - d] > lst[j]:
                        lst[j], lst[j - d] = lst[j - d], lst[j]
                    else:
                        break


def Shellsort5(lst: list):
    n = len(lst)
    for k in range(min(n.bit_length(), 63), 1, -1):
        d = ((1 << k) + (1 if k & 1 else -1)) // 3
        for i in range(n - d):
            if lst[i] > lst[i + d]:
                lst[i + d], lst[i] = lst[i], lst[i + d]
                for j in range(i, d - 1, -d):
                    if lst[j - d] > lst[j]:
                        lst[j], lst[j - d] = lst[j - d], lst[j]
                    else:
                        break


def inverted_Shellsort5(lst: list):
    n = len(lst)
    for k in range(min(n.bit_length(), 63), 1, -1):
        d = ((1 << k) + (1 if k & 1 else -1)) // 3
        for i in range(n - 1, d - 1, -1):
            if lst[i - d] > lst[i]:
                lst[i], lst[i - d] = lst[i - d], lst[i]
                for j in range(i + d, n, d):
                    if lst[j - d] > lst[j]:
                        lst[j], lst[j - d] = lst[j - d], lst[j]
                    else:
                        break


def Shellsort6(lst: list):
    n = len(lst)
    for k in range((n >> 1).bit_length() >> 1, 0, -1):
        d = ((3 << k) >> 1) + (1 << (k << 1)) + 1
        for i in range(n - d):
            if lst[i] > lst[i + d]:
                lst[i + d], lst[i] = lst[i], lst[i + d]
                for j in range(i, d - 1, -d):
                    if lst[j - d] > lst[j]:
                        lst[j], lst[j - d] = lst[j - d], lst[j]
                    else:
                        break

    for i in range(n - 1):
        if lst[i] > lst[i + 1]:
            lst[i + 1], lst[i] = lst[i], lst[i + 1]
            for j in range(i, 0, -1):
                if lst[j - 1] > lst[j]:
                    lst[j], lst[j - 1] = lst[j - 1], lst[j]
                else:
                    break


def inverted_Shellsort6(lst: list):
    n = len(lst)
    for k in range((n >> 1).bit_length() >> 1, 0, -1):
        d = ((3 << k) >> 1) + (1 << (k << 1)) + 1
        for i in range(n - 1, d - 1, -1):
            if lst[i - d] > lst[i]:
                lst[i], lst[i - d] = lst[i - d], lst[i]
                for j in range(i + d, n, d):
                    if lst[j - d] > lst[j]:
                        lst[j], lst[j - d] = lst[j - d], lst[j]
                    else:
                        break

    for i in range(n - 1, 0, -1):
        if lst[i - 1] > lst[i]:
            lst[i], lst[i - 1] = lst[i - 1], lst[i]
            for j in range(i + 1, n):
                if lst[j - 1] > lst[j]:
                    lst[j], lst[j - 1] = lst[j - 1], lst[j]
                else:
                    break


if __name__ == '__main__':
    from timeit import default_timer as timer
    import random


    def run_test(f_list: list, lst: list):
        for f in f_list:
            lst_copy = lst.copy()
            start = timer()
            f(lst_copy)
            end = timer()
            print(f'{f.__name__:60}{f"{end - start:.7f}":>12} seconds')


    n_list = [  100_000,   200_000,   500_000]

    f_list = [
        Shellsort0, inverted_Shellsort0,
        Shellsort1, inverted_Shellsort1,
        Shellsort2, inverted_Shellsort2,
        Shellsort3, inverted_Shellsort3,
        Shellsort4, inverted_Shellsort4,
        Shellsort5, inverted_Shellsort5,
        Shellsort6, inverted_Shellsort6
    ]

    for n in n_list:
        print(f'\n{f"---- The following benchmarks are for lists of size {n:^9} ----":^80}\n')

        print(f'\n{"Test for a list of uniformly distributed random integers":^80}\n')
        a = 0
        b = n * 10
        lst = [random.randint(a, b) for i in range(n)]
        run_test(f_list, lst)

        print(f'\n{"Test for a list of normally distributed random integers":^80}\n')
        m = 100
        st_dev = 9
        lst = [math.trunc(random.gauss(m, st_dev)) for i in range(n)]
        run_test(f_list, lst)

        ratio_unsorted = 0.1
        n_unsorted = round(ratio_unsorted * n)
        if n_unsorted:
            print(f'\n{"Test for the sorted list of integers extended with an unsorted list":^80}\n')
            n_unsorted_div_2 = n_unsorted >> 1
            lst = list(range(n_unsorted_div_2, n - n_unsorted_div_2))
            lst.extend([random.randint(0, n - 1) for i in range(n_unsorted)])
            run_test(f_list, lst)

        print(f'\n{"Test for a reverse-sorted list of distinct integers":^80}\n')
        lst = list(range(n - 1, -1, -1))
        run_test(f_list, lst)

        print(f'\n{"Test for an interleaved list of distinct integers":^80}\n')
        lst = list(range(n))
        lst[(n & 1) ^ 1::2] = lst[::-2]
        run_test(f_list, lst)

        print(f"""\n{'Test for the "pipe organ" list of integers':^80}\n""")
        lst = list(range((n + 1) >> 1))
        lst.extend(range((n >> 1) - 1, -1, -1))
        run_test(f_list, lst)

        print(f'\n{"Test for the sorted list of distinct integers":^80}\n')
        lst = list(range(n))
        run_test(f_list, lst)

        print(f'\n{"Test for the constant list":^80}\n')
        lst = [0] * n
        run_test(f_list, lst)

        print()
