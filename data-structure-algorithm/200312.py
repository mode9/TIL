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
    answer = -1
    lower = 0
    upper = len(L) - 1
    while lower <= upper:
        middle = (lower + upper) // 2
        if L[middle] == x:
            return middle
        elif L[middle] < x:
            lower = middle + 1
        elif L[middle] > x:
            upper = middle - 1

    return answer


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


def main():
    # lst = [1, 23, 24, 53, 2, 50, 29, 93]
    # lst.sort()
    # element = 22
    #
    # print(insert_element_into_list(lst, element))
    # lst.append(23)
    # lst.append(23)
    # lst.append(23)
    # lst.sort()
    # element = 23
    # print(search_all_element_in_list(lst, element))
    # print(solution([2, 3, 5, 6, 9], 4))
    print(fibonacci_recursive(0))
    print(fibonacci_iterative(0))
    i = 1
    x = i if i > 1 else None
    print(x)


if __name__ == '__main__':
    main()
