class ArrayStack:

    def __init__(self):
        self.data = []

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


if __name__ == '__main__':
    # S = '(A+B)*(C+D)'
    # S = 'A*(B-(C+D))'
    S = 'A+(B-C))*D'
    print(solution(S))
