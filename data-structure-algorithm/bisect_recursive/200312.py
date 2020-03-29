# Linear Array


def insert_element_into_list(L, x):
    if x < L[0]:
        L.insert(0, x)
        return L
    elif x > L[-1]:
        L.append(x)
        return L
    for index, value in enumerate(L):
        if value < x:
            continue
        elif value > x:
            L.insert(index, x)
            break

    return L


def search_all_index_in_list(L, x):
    answer = []
    is_contained = False
    index = 0

    while x in L[index:]:
        is_contained = True
        calc_index = index  # 리스트 슬라이싱 후의 인덱스 계산을 위해 저장
        index = L[index:].index(x)
        index += calc_index  # 슬라이싱된 인덱스를 전체 리스트의 인덱스로 계산
        answer.append(index)
        index += 1  # 찾아진 인덱스 이후의 원소부터 슬라이싱

    if is_contained:
        return answer
    else:
        return [-1]


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


def bisect_recursive(L, x, lower=None, upper=None):
    if not lower and not upper:
        lower = 0
        upper = len(L) - 1
    middle = (lower + upper) // 2
    if L[middle] == x:
        return middle
    elif L[middle] < x:
        lower = middle + 1
    else:
        upper = middle
    return bisect_recursive(L, x, lower, upper)


def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


def fibonacci_iterative(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a+b
    return a


if __name__ == '__main__':
    lst = [1, 3, 6, 9, 10, 20, 35, 70]
    # idx = binary_search(lst, 3)
    # print(lst[idx])
    idx = bise