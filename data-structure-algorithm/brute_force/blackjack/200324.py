# import itertools
#
#
# def get_approx_val():
#     """테스트 결과 메모리 42436 KB / 시간 132ms"""
#     num_count, target = map(int, input().split())
#     num_list = map(int, input().split())
#     case_list = list(itertools.combinations(num_list, 3))
#     approx = 0
#     for case in case_list:
#         sum_case = sum(case)
#         if sum_case > target:
#             continue
#         elif sum_case == target:
#             approx = sum_case
#             break
#         else:
#             if approx < sum_case < target:
#                 approx = sum_case
#
#     return approx
#
#
# def best_solution():
#     """테스트 결과 메모리 29284 KB / 시간 56ms"""
#     print(P(*map(int, input().split()), list(sorted(map(int, input().split()))[::-1])))
#
#
# def P(n, m, c):
#     t = set()
#     for i in range(n-2):
#         for o in range(i+1, n-1):
#             for p in range(o+1, n):
#                 s = c[i] + c[o] + c[p]
#                 if s <= m:
#                     t.add(s)
#                     break
#
#     return max([*t])


# import itertools
# import math
#
#
# def is_prime(n):
#     if n <= 1:
#         return False
#     elif n == 2:
#         return True
#     elif n % 2 == 0:
#         return False
#     for i in range(3, int(math.sqrt(n)) + 1, 2):
#         if n % i == 0:
#             return False
#
#     return True
#
#
# def solution(numbers):
#     answer = 0
#     num_lst = []
#     check_lst = []
#     for ch in numbers:
#         num_lst.append(ch)
#     for i in range(1, len(num_lst) + 1):
#         cases = itertools.permutations(num_lst, i)
#         for case in cases:
#             n = int(''.join(case))
#             if n not in check_lst and is_prime(n):
#                 check_lst.append(n)
#                 answer += 1
#
#     return answer

# import itertools
#
#
# def baseball_game(case, question):
#     strike = 0
#     ball = 0
#
#     for i in range(3):
#         if case[i] == question[i]:
#             strike += 1
#         elif question[i] in case:
#             ball += 1
#     return [strike, ball]
#
#
# def solution(baseball):
#     candidate_lst = [str(i) for i in range(1, 10)]
#     candidates = list(itertools.permutations(candidate_lst, 3))
#     for num, strike, ball in baseball:
#         num = str(num)
#         candidates = [candidate for candidate in candidates if baseball_game(num, candidate) == [strike, ball]]
#
#     return len(candidates)


# JoyStick
from string import ascii_uppercase


def solution(name):
    answer = 0
    where = 0
    m = []
    alphabet_lst = list(ascii_uppercase)
    diction = {}
    for i, j in zip(range(len(alphabet_lst) + 1), alphabet_lst):
        diction[j] = i

    for i in range(len(name)):
        middle = diction['Z'] // 2 + 1
        if diction[name[i]] >= middle:
            m.append(diction['Z'] - diction[name[i]] + 1)
        else:
            m.append(diction[name[i]])

    while True:
        answer += m[where]
        m[where] = 0
        if sum(m) == 0:
            break
        else:
            left = 1
            right = 1
            while m[where-left] <= 0:
                left += 1
            while m[where+right] <= 0:
                right += 1
            where += -left if left < right else right
            answer += left if left < right else right
            from heapq import heappush

    return answer


if __name__ == '__main__':
    # print(get_approx_val())
    # best_solution()
    # for i in range(2, 101):
    #     print(i, is_prime(i))
    # print(solution("011"))
    # arr = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]
    print(solution('BBABAAAB'))
