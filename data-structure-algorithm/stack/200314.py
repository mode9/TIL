class ArrayStack:

    def __init__(self, *args):
        self.data = [*args]

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]


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


prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}


def solution(S):
    opStack = ArrayStack()
    answer = ''
    operators = '*/+-()'

    for c in S:
        if c not in operators:
            answer += c
        else:
            if c == '(':
                opStack.push(c)
            elif c == ')':
                while not opStack.peek() == '(':
                    answer += opStack.pop()
                opStack.pop()
            elif opStack.isEmpty():
                opStack.push(c)
            else:
                if prec[c] > prec[opStack.peek()]:
                    opStack.push(c)
                else:
                    try:
                        while not prec[c] > prec[opStack.peek()]:
                            answer += opStack.pop()
                    except IndexError:
                        pass
                    opStack.push(c)
    while not opStack.isEmpty():
        answer += opStack.pop()

    return answer


S = ArrayStack()
print(S.isEmpty())
