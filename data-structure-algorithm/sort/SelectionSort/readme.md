# 선택 정렬(Selection Sort)

- 시간복잡도: O(n<sup>2</sup>)



#### 개념

- 배열을 순회하여 가장 큰/작은 수를 찾아 앞에서부터 차례대로 원소를 위치시키는 정렬 알고리즘이다.
- 순서에 따라 이동할 위치를 정해놓고, 필요한 조건에 맞는 원소를 찾아 해당 위치로 이동시킨다.



#### 예제

```python
def selection_sort(unsorted):
    last_element_count = 1
    length = len(unsorted) - last_element_count
    for i in range(length):
        target_index = i
        for j in range(i+1, length+last_element_count):
            if unsorted[target_index] > unsorted[j]:
                target_index = j
        if target_index != i:
            unsorted[i], unsorted[target_index] = unsorted[target_index], unsorted[i]
    sorted_ = unsorted
    return sorted_
```



#### 장단점

- 장점: 크기가 작은 배열의 정렬에서 효과가 좋다. 주어진 배열외의 다른 메모리 공간이 필요하지 않다.
- 단점: 큰 배열의 경우 성능이 떨어진다.



#### 참고

- [[알고리즘] 선택 정렬(selection sort)이란](https://gmlwjd9405.github.io/2018/05/06/algorithm-selection-sort.html)
- [[초보몽키의 개발공부로그](https://wayhome25.github.io/)](https://wayhome25.github.io/cs/2017/04/16/cs-17/)