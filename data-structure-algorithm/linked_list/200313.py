import collections

class Node:

    def __init__(self, item):
        self.data = item
        self.next = None

# Dummy Node
# class LinkedList:
#
#     def __init__(self):
#         self.nodeCount = 0
#         self.head = Node(None)
#         self.tail = None
#         self.head.next = self.tail
#
#     def traverse(self):
#         result = []
#         curr = self.head
#         while curr.next:
#             curr = curr.next
#             result.append(curr.data)
#         return result
#
#     def getAt(self, pos):
#         if pos < 0 or pos > self.nodeCount:
#             return None
#
#         i = 0
#         curr = self.head
#         while i < pos:
#             curr = curr.next
#             i += 1
#
#         return curr
#
#     def insertAfter(self, prev, newNode):
#         newNode.next = prev.next
#         if prev.next is None:
#             self.tail = newNode
#         prev.next = newNode
#         self.nodeCount += 1
#         return True
#
#     def insertAt(self, pos, newNode):
#         if pos < 1 or pos > self.nodeCount + 1:
#             return False
#
#         if pos != 1 and pos == self.nodeCount + 1:
#             prev = self.tail
#         else:
#             prev = self.getAt(pos - 1)
#         return self.insertAfter(prev, newNode)
#
#     def popAfter(self, prev):
#         curr = prev.next
#         if curr is None:  # prev 가 Node 의 tail 일 경우
#             return None
#         elif curr.next is None:  # curr 가 Node 의 tail 일 경우
#             self.tail = prev
#             prev.next = None
#         else:
#             prev.next = curr.next
#         self.nodeCount -= 1
#         return curr.data
#
#     def popAt(self, pos):
#         if pos < 1 or pos > self.nodeCount:
#             raise IndexError
#         prev = self.getAt(pos - 1)
#
#         return self.popAfter(prev)
#
#
# class LinkedList:
#
#     def __init__(self):
#         self.nodeCount = 0
#         self.head = Node(None)
#         self.tail = None
#         self.head.next = self.tail
#
#     def traverse(self):
#         result = []
#         curr = self.head
#         while curr.next:
#             curr = curr.next
#             result.append(curr.data)
#         return result
#
#     def getAt(self, pos):
#         if pos < 0 or pos > self.nodeCount:
#             return None
#
#         i = 0
#         curr = self.head
#         while i < pos:
#             curr = curr.next
#             i += 1
#
#         return curr
#
#     def insertAfter(self, prev, newNode):
#         newNode.next = prev.next
#         if prev.next is None:
#             self.tail = newNode
#         prev.next = newNode
#         self.nodeCount += 1
#         return True
#
#     def insertAt(self, pos, newNode):
#         if pos < 1 or pos > self.nodeCount + 1:
#             return False
#
#         if pos != 1 and pos == self.nodeCount + 1:
#             prev = self.tail
#         else:
#             prev = self.getAt(pos - 1)
#         return self.insertAfter(prev, newNode)
#
#     def popAfter(self, prev):
#         curr = prev.next
#         if curr is None:  # prev 가 Node 의 tail 일 경우
#             return None
#         elif curr.next is None:  # curr 가 Node 의 tail 일 경우
#             self.tail = prev
#             prev.next = None
#         else:
#             prev.next = curr.next
#         self.nodeCount -= 1
#         return curr.data
#
#     def popAt(self, pos):
#         if pos < 1 or pos > self.nodeCount:
#             raise IndexError
#         prev = self.getAt(pos - 1)
#
#         return self.popAfter(prev)


class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None

        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr

    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True

    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError

        prev = self.getAt(pos - 1)
        if not prev:  # pos 가 Head 일 경우
            curr = self.getAt(pos)
            self.head = curr.next if curr.next else None
            self.tail = self.tail if self.head else None  # pos 노드가 유일한 노드일 경우
        else:
            curr = prev.next
            prev.next = curr.next
            if not prev.next:  # pos 가 Tail 일 경우
                self.tail = prev

        self.nodeCount -= 1
        return curr.data

    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result

    def traverse_mine(self):
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


class DoublyLinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None

    def traverse(self):
        result = []
        curr = self.head
        while curr.next.next:
            curr = curr.next
            result.append(curr.data)
        return result

    def insertBefore(self, next, newNode):
        prev = next.prev
        if prev is None:  # head 앞에 삽입하는 경우
            return False
        newNode.next = next
        newNode.prev = prev
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True

    def reverse(self):
        result = []
        curr = self.tail.prev
        try:
            while curr.prev:
                result.append(curr.data)
                curr = curr.prev
        except AttributeError:
            pass
        return result

    # def reverse(self):
    #     result = []
    #     curr = self.tail
    #     while curr.prev.prev:
    #         curr = curr.prev
    #         result.append(curr.data)
    #     return result

    def concat(self, L):
        tail_prev = self.tail.prev
        new_next = L.head.next
        new_tail = L.tail
        if new_next == new_tail:
            tail_prev = self.tail.prev
            new_tail.prev = tail_prev
            tail_prev.next = new_tail
        else:
            tail_prev.next = new_next
            new_next.prev = tail_prev
        self.tail = new_tail
        self.nodeCount += L.nodeCount

    # def concat(self, L):
    #     tail_prev = self.tail.prev
    #     new_next = L.head.next
    #     new_tail = L.tail
    #
    #     tail_prev.next = new_next
    #     new_next.prev = tail_prev
    #
    #     self.tail = new_tail
    #     self.nodeCount += L.nodeCount


def main():
    node1 = Node(43)
    node2 = Node(85)
    node3 = Node(62)
    node1.next = node2
    node2.next = node3

    ll = LinkedList()
    ll.head = node1
    ll.tail = node3
    print(ll.traverse())


if __name__ == '__main__':
    main()

