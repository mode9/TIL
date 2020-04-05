# 영화감독 숌

from [백준](https://www.acmicpc.net/problem/1436)

#### 문제

666은 종말을 나타내는 숫자라고 한다. 따라서, 많은 블록버스터 영화에서는 666이 들어간 제목을 많이 사용한다. 영화감독 숌은 세상의 종말 이라는 시리즈 영화의 감독이다. 조지 루카스는 스타워즈를 만들 때, 스타워즈 1, 스타워즈 2, 스타워즈 3, 스타워즈 4, 스타워즈 5, 스타워즈 6과 같이 이름을 지었고, 피터 잭슨은 반지의 제왕을 만들 때, 반지의 제왕 1, 반지의 제왕 2, 반지의 제왕 3과 같이 영화 제목을 지었다.
하지만 숌은 자신이 조지 루카스와 피터 잭슨을 뛰어넘는다는 것을 보여주기 위해서 영화 제목을 좀 다르게 만들기로 했다.
종말의 숫자란 어떤 수에 6이 적어도 3개이상 연속으로 들어가는 수를 말한다. 제일 작은 종말의 숫자는 666이고, 그 다음으로 큰 수는 1666, 2666, 3666, .... 과 같다.
따라서, 숌은 첫 번째 영화의 제목은 세상의 종말 666, 두 번째 영화의 제목은 세상의 종말 1666 이렇게 이름을 지을 것이다. 일반화해서 생각하면, N번째 영화의 제목은 세상의 종말 (N번째로 작은 종말의 숫자) 와 같다.
숌이 만든 N번째 영화의 제목에 들어간 숫자를 출력하는 프로그램을 작성하시오. 숌은 이 시리즈를 항상 차례대로 만들고, 다른 영화는 만들지 않는다.

#### 입력

첫째 줄에 숫자 N이 주어진다. N은 10,000보다 작거나 같은 자연수이다.

#### 출력

첫째 줄에 N번째 영화의 제목에 들어간 수를 출력한다.



#### 내 코드

이 문제는 30분 넘게 고민했지만 정말 아이디어가 떠오르지 않았다. 

```python
n = int(input())
count = 0
i = 666
result = ''
while n != count:
    result = str(i)
    if '666' in result:
        count += 1
    i += 1
print(result)
```

그 결과 테스트케이스만 통과하고 시간은 1초 걸리는 뜨악한 나의 코드....

#### 답안 

by [leejunhaeng](https://www.acmicpc.net/user/leejunhaeng)

읽기 쉽도록 변수명을 조금 변경했다.

```python
N = int(input())
if N==1:
    print(666)
else:
    count = 1
    for i in range(2, N+1):
        movie_title = f"{0}666".format(i-1)
        num_of_extra_six_in_row = 0
        for j in range(len(movie_title) - 3):
            if movie_title[-4-j]=='6':
                num_of_extra_six_in_row += 1
            else:
                break
        count += int(10**num_of_extra_six_in_row)
        if count >= N:
            break
            
    if num_of_extra_six_in_row > 0:
        base = int(10**num_of_extra_six_in_row)
        count -= base
        movie_title = int(base_title) - int(base_title)%base + (N - count-1)
        
    print(movie_title)
```

1. 기본개념은 666을 찾을때마다 count를 1씩 증가시켜 N == count 일 때의 movie_title을 출력한다.

2. 기본 666에서 1000씩 증가하며 count += 1
   예) 666 -> 1666 -> 2666 -> n666

3. movie_title에서 "6"이 4개 이상이면(num_of_extra_six_in_row)가 존재하면 

   ```python
   count += int(10**num_of_extra_six_in_row)
   ```

   예) 6666 -> 6이 4개 -> 6660~6669(10^1개) 
         66666 ->6이 5개 -> 66600~66699(10^2개)

4. 기본적으로 count ==  N인 상태의 movie_title을 출력해야 하는데, 2번 과정을 거치면 count가 n보다 큰 상태로 for문을 빠져나오는 경우가 생긴다. 예를 들어 n이 7일 때, 

   ```python
   movie_title = f"{0}666".format(i-1)
   ```

   위 코드에 따라 1000씩 증가하기 때문에, 6번째 movie_title은 5666이고, 7번째는 6666이다. 
   6666을 만나면 아래 내용에 따라 count += 10 ** 1이 실행(count += 10), count가 16이 되어 count >= n을 만족하기 때문에 break를 만난다. 

   ```python
   for k in range(len(base_title)-3):
       if base_title[-4-k]=='6':
         num_of_extra_six_in_row += 1
       else:
         break
   count += int(10**num_of_extra_six_in_row)
   if count >= N:
   		break
   ```

   위 상황이 진행되면 N번째 movie_title은 6666이다. 그러나 내가 원하는 건 6660이다.

5. 4번 상황에서 생긴 문제를 아래 if문에서 처리하게 된다.

   ```python
   if num_of_extra_six_in_row > 0:
   		base = int(10**num_of_extra_six_in_row)
       count -= base
       base_title = int(base_title) - int(base_title)%base + (N - count-1)
   ```