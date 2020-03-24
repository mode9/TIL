포화 이진트리(Full Binary Tree)
-
모든 레벨에서 노드들이 채워져 있는 이진 트
높이(height, depth)가 k일 때, 노드의 갯수가 2^k - 1 인 이진 트리

완전 이진 트리(Complete Binary Tree)
-
높이 k인 완전 이진 트리
레벨 k-2 까지는 모든 노드가 2개의 자식을 가진 포화 이진트리이며,
레벨 k-1 에서는 왼쪽부터 노드가 순차적으로 채워져 있다면 완전 이진 트리이다.

- depth or height: 루트부터 1로 시작하여 내려감
- level: 루트부터 0으로 시작하여 내려감
- degree: 노드가 가진 자식의 갯수

1. 깊이 우선 순회(depth first traversal)
    - 중위 순회(in-order traversal): left->self->right
    - 전위 순회(pre-order traversal): self->left->right
    - 후위 순회(post-order traversal): left->right->self
2. 넓이 우선 순회(breadth first traversal)
    - 낮은 레벨의 노드순으로
    - 같은 레벨의 노드에서는 부모노드의 방문순서에 따라 방문, 왼쪽 자식 노드를 오른쪽보다 우선 방문.
    - 트리를 따라 내려가는 것이 아니라, 낮은 레벨 순으로 횡으로 방문함.
