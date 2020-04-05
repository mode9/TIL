# 블랙잭

from [백준](https://www.acmicpc.net/problem/2798)

#### 문제

각 카드에는 양의 정수가 쓰여 있다. 그 다음, 딜러는 N장의 카드를 모두 숫자가 보이도록 바닥에 놓는다. 그런 후에 딜러는 숫자 M을 크게 외친다.

이제 플레이어는 제한된 시간 안에 N장의 카드 중에서 3장의 카드를 골라야 한다. 블랙잭 변형 게임이기 때문에, 플레이어가 고른 카드의 합은 M을 넘지 않으면서 M과 최대한 가깝게 만들어야 한다.

N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.

#### 입력
첫째 줄에 카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000)이 주어진다. 둘째 줄에는 카드에 쓰여 있는 수가 주어지며, 이 값은 100,000을 넘지 않는다.

합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력으로 주어진다.

#### 출력
첫째 줄에 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력한다.


#### 나의 풀이
itertools.combinations 를 이용하여 주어진 배열에서 3장의 카드를 뽑는 중복되지 않는 모든 경우의 수를 구하여 각 케이스의 합산을 비교하여 근사값을 반환하는 함수를 구현하였다.

`테스트 결과 메모리 42436 KB / 시간 132 ms`

```python
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
```



#### 베스트 풀이
3중 for 문을 통해 카드 3장의 합계를 SET 형에 추가하여 중복값을 제외하고 마지막에 SET 형에서 최대값을 반환하는 형태.

`테스트 결과 메모리 29284 KB / 시간 56 ms`

```python
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
  
print(P(*map(int, input().split()), list(sorted(map(int, input().split()))[::-1]))
```



#### 결론
내장함수인 combinations 를 이용하여 가독성은 조금 나을 수도 있으나 결과적으로 모든 경우의 수를 연산함으로 인하여 소요시간 증가 / 결과 저장에 따른 메모리 증가로 인한 손실이 발생하였다.
