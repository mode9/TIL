# 퀵 정렬(Quick Sort)

분할 기법과 재귀함수를 이용한 정렬 알고리즘.



기준인 pivot을 중앙값으로 설정하여, pivot보다 작은 리스트와 큰 리스트를 나눠 각 리스트의 원소가 한개 남을 때까지 재귀함수를 실행시킨 후 정렬된 리스트를 반환한다.

```python
def quick_sort(arr):
  if len(arr) <= 1:
    return arr
  pivot = arr[len(arr)//2]
  lesser_arr, equal_arr, greater_arr = [], [], []
  for num in arr:
    if num < pivot:
      lesser_arr.append(num)
    elif num > pivot:
      greater_arr.append(num)
    else:
      equal_arr.append(num)
    return quicksort(lesser_arr)+equal_arr+quick_sort(greater_arr)
```

#### 시간복잡도

평균: O(nlogn)

최악: O(n<sup>2</sup>)

기준 값인 pivot보다 작은 리스트와 큰 리스트의 비율이 항상 동일하지 않기 때문에, 최악의 경우 pivot이 가장 크거나 작다면 시간복잡도가 O(n<sup>2</sup>)로 실행되게 된다.