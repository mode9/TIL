class MaxHeap:

    def __init__(self):
        self.data = [None]

    def insert(self, item):
        self.data.append(item)
        new_index = self.data.index(item)
        parent_index = new_index // 2
        while new_index > 1:
            if self.data[new_index] > self.data[parent_index]:
                self.data[new_index], self.data[parent_index] = self.data[
                                                                    parent_index], \
                                                                self.data[
                                                                    new_index]
                new_index = parent_index
                parent_index = new_index // 2
                from heapq import heappop, heappush
            else:
                break

    def remove(self):
        """
        만약 빈 Heap 이 아니라면,
         1. Heap Max 값과 Heap 의 가장 마지막 값의 위치를
         서로 바꾼 후, Max 값을 pop 한다.
         2. 이 후 앞서 임시로 위치한 값을 left, right 값들과
          대소비교를 하여, 최대 힙의 조건이 성립될 때까지
          더 큰 자식과 위치를 바꾼다.
        """
        if len(self.data) > 1:
            self.data[1], self.data[-1] = self.data[-1], self.data[1]
            data = self.data.pop(-1)
            self.maxHeapify(1)
        else:
            data = None
        return data

    def maxHeapify(self, i):
        # 왼쪽 자식 (left child) 의 인덱스를 계산합니다.
        left = 2 * i

        # 오른쪽 자식 (right child) 의 인덱스를 계산합니다.
        right = 2 * i + 1

        smallest = i
        # 왼쪽 자식이 존재하는지, 그리고 왼쪽 자식의 (키) 값이 (무엇보다?) 더 큰지를 판단합니다.
        if len(self.data) - 1 > left and self.data[left] > self.data[smallest]:
            # 조건이 만족하는 경우, smallest 는 왼쪽 자식의 인덱스를 가집니다.
            smallest = left

        # 오른쪽 자식이 존재하는지, 그리고 오른쪽 자식의 (키) 값이 (무엇보다?) 더 큰지를 판단합니다.
        if self.data[right] and self.data[right] > self.data[smallest]:
            # 조건이 만족하는 경우, smallest 는 오른쪽 자식의 인덱스를 가집니다.
            smallest = right

        if smallest != i:
            # 현재 노드 (인덱스 i) 와 최댓값 노드 (왼쪽 아니면 오른쪽 자식) 를 교체합니다.
            self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
            # 재귀적 호출을 이용하여 최대 힙의 성질을 만족할 때까지 트리를 정리합니다.
            self.maxHeapify(smallest)


def heapsort(unsorted):
    H = MaxHeap()
    for item in unsorted:
        H.insert(item)
    sorted = []
    d = H.remove()
    while d:
        sorted.append(d)
        d = H.remove()
    return sorted