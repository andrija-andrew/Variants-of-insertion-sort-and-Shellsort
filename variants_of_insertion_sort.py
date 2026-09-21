def insertion_sort(lst: list):
    for i in range(1, len(lst)):
        temp = lst[i]

        jj = 0
        for j in range(i - 1, -1, -1):
            if lst[j] > temp:
                lst[j + 1] = lst[j]
            else:
                jj = j + 1
                break

        lst[jj] = temp


def inverted_insertion_sort(lst: list):
    n = len(lst)
    for i in range(n - 2, -1, -1):
        temp = lst[i]

        jj = n - 1
        for j in range(i + 1, n):
            if lst[j] < temp:
                lst[j - 1] = lst[j]
            else:
                jj = j - 1
                break

        lst[jj] = temp


def insertion_sort_wbs(lst: list):
    for i in range(1, len(lst)):
        temp = lst[i]

        first = 0
        last = i - 1
        while first <= last:
            mid = first + ((last - first) >> 1)
            if lst[mid] <= temp:
                first = mid + 1
            else:
                last = mid - 1

        for j in range(i, first, -1):
            lst[j] = lst[j - 1]
        lst[first] = temp


def inverted_insertion_sort_wbs(lst: list):
    n_minus_1 = len(lst) - 1
    for i in range(n_minus_1 - 1, -1, -1):
        temp = lst[i]

        first = i + 1
        last = n_minus_1
        while first <= last:
            mid = first + ((last - first) >> 1)
            if lst[mid] >= temp:
                last = mid - 1
            else:
                first = mid + 1

        for j in range(i, last):
            lst[j] = lst[j + 1]
        lst[last] = temp


def _insertion_sort(lst: list):
    for i in range(1, len(lst)):
        temp = lst[i]

        jj = 0
        for j in range(i - 1, -1, -1):
            if lst[j] <= temp:
                jj = j + 1
                break

        lst[(jj + 1):(i + 1)] = lst[jj:i]
        lst[jj] = temp


def _inverted_insertion_sort(lst: list):
    n = len(lst)
    for i in range(n - 2, -1, -1):
        temp = lst[i]

        jj = n - 1
        for j in range(i + 1, n):
            if lst[j] >= temp:
                jj = j - 1
                break

        lst[i:jj] = lst[(i + 1):(jj + 1)]
        lst[jj] = temp


def _insertion_sort_wbs(lst: list):
    for i in range(1, len(lst)):
        temp = lst[i]

        first = 0
        last = i - 1
        while first <= last:
            mid = first + ((last - first) >> 1)
            if lst[mid] <= temp:
                first = mid + 1
            else:
                last = mid - 1

        lst[(first + 1):(i + 1)] = lst[first:i]
        lst[first] = temp


def _inverted_insertion_sort_wbs(lst: list):
    n_minus_1 = len(lst) - 1
    for i in range(n_minus_1 - 1, -1, -1):
        temp = lst[i]

        first = i + 1
        last = n_minus_1
        while first <= last:
            mid = first + ((last - first) >> 1)
            if lst[mid] >= temp:
                last = mid - 1
            else:
                first = mid + 1

        lst[i:last] = lst[(i + 1):(last + 1)]
        lst[last] = temp


def __insertion_sort(lst: list):
    for i in range(1, len(lst)):
        temp = lst[i]

        jj = 0
        for j in range(i - 1, -1, -1):
            if lst[j] <= temp:
                jj = j + 1
                break

        lst.insert(jj, lst.pop(i))


def __inverted_insertion_sort(lst: list):
    n = len(lst)
    for i in range(n - 2, -1, -1):
        temp = lst[i]

        jj = n - 1
        for j in range(i + 1, n):
            if lst[j] >= temp:
                jj = j - 1
                break

        lst.insert(jj, lst.pop(i))


def __insertion_sort_wbs(lst: list):
    for i in range(1, len(lst)):
        temp = lst[i]

        first = 0
        last = i - 1
        while first <= last:
            mid = first + ((last - first) >> 1)
            if lst[mid] <= temp:
                first = mid + 1
            else:
                last = mid - 1

        lst.insert(first, lst.pop(i))


def __inverted_insertion_sort_wbs(lst: list):
    n_minus_1 = len(lst) - 1
    for i in range(n_minus_1 - 1, -1, -1):
        temp = lst[i]

        first = i + 1
        last = n_minus_1
        while first <= last:
            mid = first + ((last - first) >> 1)
            if lst[mid] >= temp:
                last = mid - 1
            else:
                first = mid + 1

        lst.insert(last, lst.pop(i))


def merge_like_insertion_sort(lst: list, start: int, stop: int):
    n = stop - start
    if n > 1:
        mid = start + (n >> 1)

        merge_like_insertion_sort(lst, start, mid)
        merge_like_insertion_sort(lst, mid, stop)

        for i in range(mid, stop):
            temp = lst[i]

            jj = start
            for j in range(i - 1, start - 1, -1):
                if lst[j] > temp:
                    lst[j + 1] = lst[j]
                else:
                    jj = j + 1
                    break

            if jj < i:
                lst[jj] = temp
            else:
                return


def merge_like_inverted_insertion_sort(lst: list, start: int, stop: int):
    n = stop - start
    if n > 1:
        mid = start + (n >> 1)

        merge_like_inverted_insertion_sort(lst, start, mid)
        merge_like_inverted_insertion_sort(lst, mid, stop)

        for i in range(mid - 1, start - 1, -1):
            temp = lst[i]

            jj = stop - 1
            for j in range(i + 1, stop):
                if lst[j] < temp:
                    lst[j - 1] = lst[j]
                else:
                    jj = j - 1
                    break

            if i < jj:
                lst[jj] = temp
            else:
                return


def merge_like_insertion_sort_wbs(lst: list, start: int, stop: int):
    n = stop - start
    if n > 1:
        mid = start + (n >> 1)

        merge_like_insertion_sort_wbs(lst, start, mid)
        merge_like_insertion_sort_wbs(lst, mid, stop)

        at_least = start
        for i in range(mid, stop):
            temp = lst[i]

            first = at_least
            last = i - 1
            while first <= last:
                m = first + ((last - first) >> 1)
                if lst[m] <= temp:
                    first = m + 1
                else:
                    last = m - 1

            if first < i:
                for j in range(i, first, -1):
                    lst[j] = lst[j - 1]
                lst[first] = temp
                at_least = first + 1
            else:
                return


def merge_like_inverted_insertion_sort_wbs(lst: list, start: int, stop: int):
    n = stop - start
    if n > 1:
        mid = start + (n >> 1)

        merge_like_inverted_insertion_sort_wbs(lst, start, mid)
        merge_like_inverted_insertion_sort_wbs(lst, mid, stop)

        at_most = stop - 1
        for i in range(mid - 1, start - 1, -1):
            temp = lst[i]

            first = i + 1
            last = at_most
            while first <= last:
                m = first + ((last - first) >> 1)
                if lst[m] >= temp:
                    last = m - 1
                else:
                    first = m + 1

            if i < last:
                for j in range(i, last):
                    lst[j] = lst[j + 1]
                lst[last] = temp
                at_most = last - 1
            else:
                return


def _merge_like_insertion_sort(lst: list, start: int, stop: int):
    n = stop - start
    if n > 1:
        mid = start + (n >> 1)

        _merge_like_insertion_sort(lst, start, mid)
        _merge_like_insertion_sort(lst, mid, stop)

        for i in range(mid, stop):
            temp = lst[i]

            jj = start
            for j in range(i - 1, start - 1, -1):
                if lst[j] <= temp:
                    jj = j + 1
                    break

            if jj < i:
                lst[(jj + 1):(i + 1)] = lst[jj:i]
                lst[jj] = temp
            else:
                return


def _merge_like_inverted_insertion_sort(lst: list, start: int, stop: int):
    n = stop - start
    if n > 1:
        mid = start + (n >> 1)

        _merge_like_inverted_insertion_sort(lst, start, mid)
        _merge_like_inverted_insertion_sort(lst, mid, stop)

        for i in range(mid - 1, start - 1, -1):
            temp = lst[i]

            jj = stop - 1
            for j in range(i + 1, stop):
                if lst[j] >= temp:
                    jj = j - 1
                    break

            if i < jj:
                lst[i:jj] = lst[(i + 1):(jj + 1)]
                lst[jj] = temp
            else:
                return


def _merge_like_insertion_sort_wbs(lst: list, start: int, stop: int):
    n = stop - start
    if n > 1:
        mid = start + (n >> 1)

        _merge_like_insertion_sort_wbs(lst, start, mid)
        _merge_like_insertion_sort_wbs(lst, mid, stop)

        at_least = start
        for i in range(mid, stop):
            temp = lst[i]

            first = at_least
            last = i - 1
            while first <= last:
                m = first + ((last - first) >> 1)
                if lst[m] <= temp:
                    first = m + 1
                else:
                    last = m - 1

            if first < i:
                lst[(first + 1):(i + 1)] = lst[first:i]
                lst[first] = temp
                at_least = first + 1
            else:
                return


def _merge_like_inverted_insertion_sort_wbs(lst: list, start: int, stop: int):
    n = stop - start
    if n > 1:
        mid = start + (n >> 1)

        _merge_like_inverted_insertion_sort_wbs(lst, start, mid)
        _merge_like_inverted_insertion_sort_wbs(lst, mid, stop)

        at_most = stop - 1
        for i in range(mid - 1, start - 1, -1):
            temp = lst[i]

            first = i + 1
            last = at_most
            while first <= last:
                m = first + ((last - first) >> 1)
                if lst[m] >= temp:
                    last = m - 1
                else:
                    first = m + 1

            if i < last:
                lst[i:last] = lst[(i + 1):(last + 1)]
                lst[last] = temp
                at_most = last - 1
            else:
                return


def __merge_like_insertion_sort(lst: list, start: int, stop: int):
    n = stop - start
    if n > 1:
        mid = start + (n >> 1)

        __merge_like_insertion_sort(lst, start, mid)
        __merge_like_insertion_sort(lst, mid, stop)

        for i in range(mid, stop):
            temp = lst[i]

            jj = start
            for j in range(i - 1, start - 1, -1):
                if lst[j] <= temp:
                    jj = j + 1
                    break

            if jj < i:
                lst.insert(jj, lst.pop(i))
            else:
                return


def __merge_like_inverted_insertion_sort(lst: list, start: int, stop: int):
    n = stop - start
    if n > 1:
        mid = start + (n >> 1)

        __merge_like_inverted_insertion_sort(lst, start, mid)
        __merge_like_inverted_insertion_sort(lst, mid, stop)

        for i in range(mid - 1, start - 1, -1):
            temp = lst[i]

            jj = stop - 1
            for j in range(i + 1, stop):
                if lst[j] >= temp:
                    jj = j - 1
                    break

            if i < jj:
                lst.insert(jj, lst.pop(i))
            else:
                return


def __merge_like_insertion_sort_wbs(lst: list, start: int, stop: int):
    n = stop - start
    if n > 1:
        mid = start + (n >> 1)

        __merge_like_insertion_sort_wbs(lst, start, mid)
        __merge_like_insertion_sort_wbs(lst, mid, stop)

        at_least = start
        for i in range(mid, stop):
            temp = lst[i]

            first = at_least
            last = i - 1
            while first <= last:
                m = first + ((last - first) >> 1)
                if lst[m] <= temp:
                    first = m + 1
                else:
                    last = m - 1

            if first < i:
                lst.insert(first, lst.pop(i))
                at_least = first + 1
            else:
                return


def __merge_like_inverted_insertion_sort_wbs(lst: list, start: int, stop: int):
    n = stop - start
    if n > 1:
        mid = start + (n >> 1)

        __merge_like_inverted_insertion_sort_wbs(lst, start, mid)
        __merge_like_inverted_insertion_sort_wbs(lst, mid, stop)

        at_most = stop - 1
        for i in range(mid - 1, start - 1, -1):
            temp = lst[i]

            first = i + 1
            last = at_most
            while first <= last:
                m = first + ((last - first) >> 1)
                if lst[m] >= temp:
                    last = m - 1
                else:
                    first = m + 1

            if i < last:
                lst.insert(last, lst.pop(i))
                at_most = last - 1
            else:
                return


def unidirectional_insertion_sort(lst: list):
    for i in range(1, len(lst)):
        temp = lst[i]
        for j in range(i):
            if lst[j] > temp:
                for k in range(i, j, -1):
                    lst[k] = lst[k - 1]
                lst[j] = temp
                break


def inverted_unidirectional_insertion_sort(lst: list):
    n_minus_1 = len(lst) - 1
    for i in range(n_minus_1 - 1, -1, -1):
        temp = lst[i]
        for j in range(n_minus_1, i, -1):
            if lst[j] < temp:
                for k in range(i, j):
                    lst[k] = lst[k + 1]
                lst[j] = temp
                break


def _unidirectional_insertion_sort(lst: list):
    for i in range(1, len(lst)):
        temp = lst[i]
        for j in range(i):
            if lst[j] > temp:
                lst[(j + 1):(i + 1)] = lst[j:i]
                lst[j] = temp
                break


def _inverted_unidirectional_insertion_sort(lst: list):
    n_minus_1 = len(lst) - 1
    for i in range(n_minus_1 - 1, -1, -1):
        temp = lst[i]
        for j in range(n_minus_1, i, -1):
            if lst[j] < temp:
                lst[i:j] = lst[(i + 1):(j + 1)]
                lst[j] = temp
                break


def __unidirectional_insertion_sort(lst: list):
    for i in range(1, len(lst)):
        temp = lst[i]
        for j in range(i):
            if lst[j] > temp:
                lst.insert(j, lst.pop(i))
                break


def __inverted_unidirectional_insertion_sort(lst: list):
    n_minus_1 = len(lst) - 1
    for i in range(n_minus_1 - 1, -1, -1):
        temp = lst[i]
        for j in range(n_minus_1, i, -1):
            if lst[j] < temp:
                lst.insert(j, lst.pop(i))
                break


def merge_like_unidirectional_insertion_sort(lst: list, start: int, stop: int):
    n = stop - start
    if n > 1:
        mid = start + (n >> 1)

        merge_like_unidirectional_insertion_sort(lst, start, mid)
        merge_like_unidirectional_insertion_sort(lst, mid, stop)

        stop -= 1
        while True:
            temp = lst[mid]
            while lst[start] <= temp:
                start += 1
                if start >= mid:
                    return

            for i in range(mid, start, -1):
                lst[i] = lst[i - 1]
            lst[start] = temp

            if mid < stop:
                mid += 1
                start += 1
            else:
                return


def merge_like_inverted_unidirectional_insertion_sort(lst: list, start: int, stop: int):
    n = stop - start
    if n > 1:
        mid = start + (n >> 1)

        merge_like_inverted_unidirectional_insertion_sort(lst, start, mid)
        merge_like_inverted_unidirectional_insertion_sort(lst, mid, stop)

        stop -= 1
        mid -= 1
        while True:
            temp = lst[mid]
            while lst[stop] >= temp:
                stop -= 1
                if stop <= mid:
                    return

            for i in range(mid, stop):
                lst[i] = lst[i + 1]
            lst[stop] = temp

            if start < mid:
                mid -= 1
                stop -= 1
            else:
                return


def _merge_like_unidirectional_insertion_sort(lst: list, start: int, stop: int):
    n = stop - start
    if n > 1:
        mid = start + (n >> 1)

        _merge_like_unidirectional_insertion_sort(lst, start, mid)
        _merge_like_unidirectional_insertion_sort(lst, mid, stop)

        stop -= 1
        while True:
            temp = lst[mid]
            while lst[start] <= temp:
                start += 1
                if start >= mid:
                    return

            lst[(start + 1):(mid + 1)] = lst[start:mid]
            lst[start] = temp

            if mid < stop:
                mid += 1
                start += 1
            else:
                return


def _merge_like_inverted_unidirectional_insertion_sort(lst: list, start: int, stop: int):
    n = stop - start
    if n > 1:
        mid = start + (n >> 1)

        _merge_like_inverted_unidirectional_insertion_sort(lst, start, mid)
        _merge_like_inverted_unidirectional_insertion_sort(lst, mid, stop)

        stop -= 1
        mid -= 1
        while True:
            temp = lst[mid]
            while lst[stop] >= temp:
                stop -= 1
                if stop <= mid:
                    return

            lst[mid:stop] = lst[(mid + 1):(stop + 1)]
            lst[stop] = temp

            if start < mid:
                mid -= 1
                stop -= 1
            else:
                break


def __merge_like_unidirectional_insertion_sort(lst: list, start: int, stop: int):
    n = stop - start
    if n > 1:
        mid = start + (n >> 1)

        __merge_like_unidirectional_insertion_sort(lst, start, mid)
        __merge_like_unidirectional_insertion_sort(lst, mid, stop)

        stop -= 1
        while True:
            temp = lst[mid]
            while lst[start] <= temp:
                start += 1
                if start >= mid:
                    return

            lst.insert(start, lst.pop(mid))

            if mid < stop:
                mid += 1
                start += 1
            else:
                return


def __merge_like_inverted_unidirectional_insertion_sort(lst: list, start: int, stop: int):
    n = stop - start
    if n > 1:
        mid = start + (n >> 1)

        __merge_like_inverted_unidirectional_insertion_sort(lst, start, mid)
        __merge_like_inverted_unidirectional_insertion_sort(lst, mid, stop)

        stop -= 1
        mid -= 1
        while True:
            temp = lst[mid]
            while lst[stop] >= temp:
                stop -= 1
                if stop <= mid:
                    return

            lst.insert(stop, lst.pop(mid))

            if start < mid:
                mid -= 1
                stop -= 1
            else:
                return


def unidirectional_swap_based_insertion_sort(lst: list):
    for i in range(1, len(lst)):
        temp = lst[i]
        for j in range(i):
            if lst[j] > temp:
                lst[i] = lst[j]
                lst[j] = temp
                temp = lst[i]


def inverted_unidirectional_swap_based_insertion_sort(lst: list):
    n_minus_1 = len(lst) - 1
    for i in range(n_minus_1 - 1, -1, -1):
        temp = lst[i]
        for j in range(n_minus_1, i, -1):
            if lst[j] < temp:
                lst[i] = lst[j]
                lst[j] = temp
                temp = lst[i]


def i_cant_believe_it_can_sort(lst: list):
    n = len(lst)
    for i in range(n):
        temp = lst[i]
        for j in range(n):
            if lst[j] > temp:
                lst[i] = lst[j]
                lst[j] = temp
                temp = lst[i]


def inverted_i_cant_believe_it_can_sort(lst: list):
    n_minus_1 = len(lst) - 1
    for i in range(n_minus_1, -1, -1):
        temp = lst[i]
        for j in range(n_minus_1, -1, -1):
            if lst[j] < temp:
                lst[i] = lst[j]
                lst[j] = temp
                temp = lst[i]


def swap_based_insertion_sort(lst: list):
    for i in range(1, len(lst)):
        for j in range(i, 0, -1):
            if lst[j - 1] > lst[j]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]
            else:
                break


def inverted_swap_based_insertion_sort(lst: list):
    n_minus_1 = len(lst) - 1
    for i in range(n_minus_1 - 1, -1, -1):
        for j in range(i, n_minus_1):
            if lst[j] > lst[j + 1]:
                lst[j + 1], lst[j] = lst[j], lst[j + 1]
            else:
                break


def gnome_sort(lst: list):
    n = len(lst)
    i = 1
    while i < n:
        if lst[i - 1] <= lst[i]:
            i += 1
        else:
            lst[i - 1], lst[i] = lst[i], lst[i - 1]
            if i > 1:
                i -= 1


def inverted_gnome_sort(lst: list):
    stop = len(lst) - 1
    i = stop
    while i > 0:
        if lst[i - 1] <= lst[i]:
            i -= 1
        else:
            lst[i - 1], lst[i] = lst[i], lst[i - 1]
            if i < stop:
                i += 1


def jumping_gnome_sort(lst: list):
    n = len(lst)
    i, j = 0, 0
    while i < n:
        if i == 0 or lst[i - 1] <= lst[i]:
            if i < j:
                i = j
            i += 1
            j += 1
        else:
            lst[i - 1], lst[i] = lst[i], lst[i - 1]
            i -= 1


def inverted_jumping_gnome_sort(lst: list):
    n = len(lst)
    j = n - 1
    i = j
    while i > 0:
        if i == n or lst[i - 1] <= lst[i]:
            if j < i:
                i = j
            j -= 1
            i -= 1
        else:
            lst[i - 1], lst[i] = lst[i], lst[i - 1]
            i += 1


def sifting_sort(lst: list):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            lst[i + 1], lst[i] = lst[i], lst[i + 1]
            for j in range(i, 0, -1):
                if lst[j - 1] > lst[j]:
                    lst[j], lst[j - 1] = lst[j - 1], lst[j]
                else:
                    break


def inverted_sifting_sort(lst: list):
    n = len(lst)
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
    import math


    def run_test(f_list: list, lst: list):
        for f in f_list:
            lst_copy = lst.copy()
            if 'merge_like' not in f.__name__:
                start = timer()
                f(lst_copy)
                end = timer()
            else:
                start = timer()
                f(lst_copy, 0, len(lst_copy))
                end = timer()
            print(f'{f.__name__:55}{f"{end - start:.7f}":>12} seconds')


    n_list = [   10_000,    20_000]
    #''' <---
    f_list = [

                                  insertion_sort,                           inverted_insertion_sort,
                              insertion_sort_wbs,                       inverted_insertion_sort_wbs,
                       merge_like_insertion_sort,                merge_like_inverted_insertion_sort,
                   merge_like_insertion_sort_wbs,            merge_like_inverted_insertion_sort_wbs,
                   unidirectional_insertion_sort,            inverted_unidirectional_insertion_sort,
        merge_like_unidirectional_insertion_sort, merge_like_inverted_unidirectional_insertion_sort,
        unidirectional_swap_based_insertion_sort, inverted_unidirectional_swap_based_insertion_sort,
                      i_cant_believe_it_can_sort,               inverted_i_cant_believe_it_can_sort,
                       swap_based_insertion_sort,                inverted_swap_based_insertion_sort,
                                      gnome_sort,                               inverted_gnome_sort,
                              jumping_gnome_sort,                       inverted_jumping_gnome_sort,
                                    sifting_sort,                             inverted_sifting_sort
    ]
    '''
    f_list = [

                                    insertion_sort,                             inverted_insertion_sort,
                                insertion_sort_wbs,                         inverted_insertion_sort_wbs,
                                   _insertion_sort,                            _inverted_insertion_sort,
                               _insertion_sort_wbs,                        _inverted_insertion_sort_wbs,
                                  __insertion_sort,                           __inverted_insertion_sort,
                              __insertion_sort_wbs,                       __inverted_insertion_sort_wbs,
                         merge_like_insertion_sort,                  merge_like_inverted_insertion_sort,
                     merge_like_insertion_sort_wbs,              merge_like_inverted_insertion_sort_wbs,
                        _merge_like_insertion_sort,                 _merge_like_inverted_insertion_sort,
                    _merge_like_insertion_sort_wbs,             _merge_like_inverted_insertion_sort_wbs,
                       __merge_like_insertion_sort,                __merge_like_inverted_insertion_sort,
                   __merge_like_insertion_sort_wbs,            __merge_like_inverted_insertion_sort_wbs,
                     unidirectional_insertion_sort,              inverted_unidirectional_insertion_sort,
                    _unidirectional_insertion_sort,             _inverted_unidirectional_insertion_sort,
                   __unidirectional_insertion_sort,            __inverted_unidirectional_insertion_sort,
          merge_like_unidirectional_insertion_sort,   merge_like_inverted_unidirectional_insertion_sort,
         _merge_like_unidirectional_insertion_sort,  _merge_like_inverted_unidirectional_insertion_sort,
        __merge_like_unidirectional_insertion_sort, __merge_like_inverted_unidirectional_insertion_sort,
          unidirectional_swap_based_insertion_sort,   inverted_unidirectional_swap_based_insertion_sort,
                        i_cant_believe_it_can_sort,                 inverted_i_cant_believe_it_can_sort,
                         swap_based_insertion_sort,                  inverted_swap_based_insertion_sort,
                                        gnome_sort,                                 inverted_gnome_sort,
                                jumping_gnome_sort,                         inverted_jumping_gnome_sort,
                                      sifting_sort,                               inverted_sifting_sort
    ]
    #'''
    for n in n_list:
        print(f'\n{f"---- The following tests are for lists of size {n:^9} ----":^75}')

        print(f'\n{"Test for a list of uniformly distributed random integers":^75}\n')
        a = 0
        b = n * 10
        lst = [random.randint(a, b) for i in range(n)]
        run_test(f_list, lst)

        print(f'\n{"Test for a list of normally distributed random integers":^75}\n')
        m = 100
        st_dev = 9
        lst = [math.trunc(random.gauss(m, st_dev)) for i in range(n)]
        run_test(f_list, lst)

        ratio_unsorted = 0.1
        n_unsorted = round(ratio_unsorted * n)
        if n_unsorted:
            print(f'\n{"Test for the sorted list of integers extended with an unsorted list":^75}\n')
            n_unsorted_div_2 = n_unsorted >> 1
            lst = list(range(n_unsorted_div_2, n - n_unsorted_div_2))
            lst.extend([random.randint(0, n - 1) for i in range(n_unsorted)])
            run_test(f_list, lst)

        print(f'\n{"Test for a reverse-sorted list of distinct integers":^75}\n')
        lst = list(range(n - 1, -1, -1))
        run_test(f_list, lst)

        print(f'\n{"Test for an interleaved list of distinct integers":^75}\n')
        lst = list(range(n))
        lst[(n & 1) ^ 1::2] = lst[::-2]
        run_test(f_list, lst)

        print(f"""\n{'Test for the "pipe organ" list of integers':^75}\n""")
        lst = list(range((n + 1) >> 1))
        lst.extend(range((n >> 1) - 1, -1, -1))
        run_test(f_list, lst)

        print(f'\n{"Test for the sorted list of distinct integers":^75}\n')
        lst = list(range(n))
        run_test(f_list, lst)

        print(f'\n{"Test for the constant list":^75}\n')
        lst = [0] * n
        run_test(f_list, lst)
