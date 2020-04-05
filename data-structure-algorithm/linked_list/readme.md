링크드리스트
------
|                    |   배열   | 링크드리스트 |
| ------------------ | :------: | :----------: |
| `저장공간(메모리)` | 연속위치 |   임의위치   |
| `원소탐색`         | 매우간편 |   선형탐색   |
| `삽입/삭제`        |   느림   |   매우간편   |

1. 저장공간
    - 배열의 경우 각 원소들의 메모리 위치가 연속적.
    - 링크드리스트는 위치가 무작위.
2. 원소탐색
    - 배열은 인덱스만 있으면 O(1)로 매우 간편하게 접근할 수 있다.
    - 링크드리스트는 기본적으로 선형탐색의 형태로 접근한다. head/tail 은 O(1)
3. 삽입/삭제
    - 배열은 삽입/삭제 시 해당 인덱스 이후의 모든 원소의 위치를 당기거나 미루는 작업이 필요하며, 할당된 메모리가 부족할 경우 메모리를 추가 할당해야한다.
    - 링크드리스트는 prev,next 의 주소만 변경하면 되므로 매우 간편하다.
    

* 모든 노드를 탐색하여 데이터 리스트를 반환하는 함수를 구현하였다. 다이어트할 부분이 많다.
```python
def traverse(self):
    curr = self.head
    if not curr:
        return []
    result = []
    while True:
        result.append(curr.data)
        if not curr.next:
            break
        curr = curr.next
    return result
```

* Better
    * curr를 체크하는 두가지 if문을 while 조건문으로 줄인 모습이 훨씬 깔끔하고 가독성이 좋아보인다.
```python
def traverse(self):
    result = []
    curr = self.head
    while curr is not None:
        result.append(curr.data)
        curr = curr.next
    return result
```

* 더블 링크드리스트를 결합하는 함수.
```python
def concat(self, L):
    old_last = self.tail.prev
    new_next = L.head.next
    new_tail = L.tail
    if new_next == new_tail:
        new_tail.prev = old_last
        old_last.next = new_tail
    else:
        old_last.next = new_next
        new_next.prev = old_last
    self.tail = new_tail
    self.nodeCount += L.nodeCount
```
* Better
    * 더미헤드와 더미테일이 있기 때문에 입력받은 링크드리스트(L)가 비었다면 더미 head.next == 더미 tail 이다. 
    
    ```python
    if new_next == new_tail:
            new_tail.prev = old_last
            old_last.next = new_tail
    ```
    위 구문은 L이 비었을 경우 old_last_node <--> new_dummy_tail 를 연결하는 코드인데,
    위에서 설명한 바와 같이 결과적으로 L이 빈 경우에도 new_next 는 더미 tail 을 가리키게 되므로 
    ```python
    new_tail.prev = old_last
    new_next.prev = old_last
    
    old_last.next = new_tail 
    old_last.next = new_next 
    ```
    빈 L이 입력되면 위 두 줄은 같다. 따라서 if 문은 필요없는 코드다.
```python
def concat(self, L):
    old_last = self.tail.prev
    new_next = L.head.next
    new_tail = L.tail

    old_last.next = new_next
    new_next.prev = old_last

    self.tail = new_tail
    self.nodeCount += L.nodeCount
```
