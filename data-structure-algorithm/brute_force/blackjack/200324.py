import itertools


def get_approx_val():
    """테스트 결과 메모리 42436 KB / 시간 132ms"""
    num_count, target = map(int, input().split())
    num_list = map(int, input().split())
    case_list = list(itertools.combinations(num_list, 3))
    approx = 0
    for case in case_list:
        sum_case = sum(case)
        if sum_case > target:
            continue
        elif sum_case == target:
            approx = sum_case
            break
        else:
            if approx < sum_case < target:
                approx = sum_case

    return approx


def best_solution():
    """테스트 결과 메모리 29284 KB / 시간 56ms"""
    print(P(*map(int, input().split()), list(sorted(map(int, input().split()))[::-1])))


def P(n, m, c):
    t = set()
    for i in range(n-2):
        for o in range(i+1, n-1):
            for p in range(o+1, n):
                s = c[i] + c[o] + c[p]
                if s <= m:
                    t.add(s)
                    break

    return max([*t])


if __name__ == '__main__':
    # print(get_approx_val())
    best_solution()
