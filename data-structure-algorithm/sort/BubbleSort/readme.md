# 버블 정렬(Bubble Sort)

- 서로 인접한 두 원소를 검사하여 정렬하는 알고리즘
- 인접한 2개의 레코드를 비교하여 크기가 순서대로 되어 있지 않으면 서로 교환한다.
- 시간복잡도 O(n<sup>2</sup>)



#### 개념

1. 첫 번째 자료와 두 번째 자료, 두 번째 자료와 세 번째 자료, 세 번째와 네 번째... 배열의 마지막 원소까지 차례대로 인접한 두개의 원소를 비교하여 정렬하는 알고리즘이다.

2. 배열을 한 바퀴 순회하게 되면 가장 큰/작은 원소가 배열의 마지막 인덱스에 위치하게 되는데, 이후 마지막 원소를 제외한 남은 배열을 다시 1번으로 돌아가 정렬하여, 배열의 원소가 한 개 남을 때까지 순회하며 비교 정렬한다.



#### 예제

```python
def bubble_sort(unsorted):
    last_element_count = 1
    length = len(unsorted) - last_element_count
    for i in range(length):
        for j in range(length-i):
            if unsorted[j] > unsorted[j+1]:
                unsorted[j], unsorted[j+1] = unsorted[j+1], unsorted[j]
		sorted_ = unsorted
		return sorted_
```



#### 장단점

- 장점: 구현이 간편하다.
- 단점: 원소간의 인덱스 변경, 즉 자리이동이 빈번하게 발생하므로 비효율적이다.

#### 참고

[[알고리즘] 버블 정렬(bubble sort)이란](https://gmlwjd9405.github.io/2018/05/06/algorithm-bubble-sort.html)