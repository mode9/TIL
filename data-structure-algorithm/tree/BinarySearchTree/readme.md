# 이진 탐색 트리(Binary Search Tree)

​    모든 노드에 대해서 왼쪽 서브트리에 있는 데이터는 모두 부모노드의 값보다 작고,
​    오른쪽 서브트리에 있는 데이터는 모두 보모노드의 값보다 큰 성질을 만족하는 이진 트리.
​    

- 장점: 데이터 원소의 추가/삭제가 용이
- 단점: 공간 소요가 큼
- 시간복잡도: O(logn)

- 연산:
    - insert(key, data): 트리에 주어진 원소를 추가
    - remove(key): 특정 원소를 트리에서 삭제
    - lookup(key): 특정 원소를 검색
    - inorder(): 키의 순서대로 원소를 반환
    - min(), max(): 최소값, 최대값