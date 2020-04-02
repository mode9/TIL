def binary_search(L, x):
    lower = 0
    upper = len(L) - 1
    while lower <= upper:
        middle = (lower + upper) // 2
        if L[middle] < x:
            lower = middle + 1
        else:
            upper = middle

    return lower


def bisect_recursive(L, x):
    if len(L) == 0:
        return False
    mid = len(L) // 2
    if L[mid] == x:
        return mid
    else:
        if x < L[mid]:
            return bisect_recursive(L[:mid], x)
        else:
            return bisect_recursive(L[mid+1:], x)
