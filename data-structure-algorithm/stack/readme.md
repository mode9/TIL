# 스택

- 후입선출(LIFO) 원칙의 자료구조

1. 스택오버플로우: 이미 가득 찬 스택에 원소를 더 넣으려고 하면 발생하는 오류
2. 스택언더플로우: 빈 스택에서 원소를 꺼내려는 시도를 하는 경우 발생하는 오류

* 스택의 자료구조 형태
    1. 배열을 이용한 구현
    2. 링크드리스트를 이용한 구현
    3. 연산: size(), is_empty(), push(), pop(), peek()[마지막 원소를 제거하지않고 반환]
    



#### 사용 사례

1. 재귀 알고리즘
2. 방문 기록
3. 실행 기록
4. 문자열 뒤집기
5. 수식의 괄호검사
6. 후위 표기법



#### 파이썬 구현

- ArrayStack

```python
class Stack:
  def __init__(self, *args):
    self.items = [*args]
  
  def push(item):
    self.items.append(item)
    
  def size():
    return len(self.items)
  
  def is_empty():
    return self.size() == 0
  
  def pop():
    return self.items.pop()
  
  def peek():
    return self.items[-1]
```

- LinkedList Stack

```python
class Node:
    def __init__(self, item):
        self.data = item
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node

    def size(self):
        if self.head is None:
            return 0
        else:
            count = 0
            node = self.head
            while node is not None:
                node = node.next
                count += 1
            return count

    def is_empty(self):
        return self.head is None

    def pop(self):
        node = self.head
        if node:
            self.head = node.next

        return node.data

    def peek(self):
        if self.is_empty():
            return -1
        return self.head.data
```

