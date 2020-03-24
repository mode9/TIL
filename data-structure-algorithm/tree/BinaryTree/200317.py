class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None

    def size(self):
        """루트 +1"""
        l = self.left.size() if self.left else 0
        r = self.right.size() if self.right else 0
        return l + r + 1

    def depth(self):
        """루트를 1로 시작하여 내려가므로 +1을 해준다."""
        l = self.left.depth() if self.left else 0
        r = self.right.depth() if self.right else 0
        return l + 1 if l > r else r + 1

    def inorder(self):
        """Left -> Self -> Right"""
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self.data)
        if self.right:
            traversal += self.right.inorder()
        return traversal

    def preorder(self):
        """Self -> Left -> Right"""
        traversal = [self.data]
        if self.left:
            traversal += self.left.preorder()
        if self.right:
            traversal += self.right.preorder()
        return traversal

    def postorder(self):
        """Left -> Right -> self"""
        traversal = []
        if self.left:
            traversal += self.left.postorder()
        if self.right:
            traversal += self.right.postorder()
        traversal.append(self.data)
        return traversal


class BinaryTree:

    def __init__(self, r):
        self.root = r

    def size(self):
        if self.root:
            return self.root.size()
        else:
            return 0

    def depth(self):
        if self.root:
            return self.root.depth()
        else:
            return 0

    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []

    def preorder(self):
        if self.root:
            return self.root.preorder()
        else:
            return []

    def postorder(self):
        if self.root:
            return self.root.postorder()
        else:
            return []

    def bft(self):
        """낮은 레벨부터, 좌측부터"""
        traverse = []
        q = ArrayQueue()
        if self.root:
            q.enqueue(self.root)
        while not q.isEmpty():
            curr = q.dequeue()
            traverse.append(curr.data)
            if curr.left:
                q.enqueue(curr.left)
            if curr.right:
                q.enqueue(curr.right)
        return traverse


class ArrayQueue:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]