# BFS랑은 다르게 한 우물만 판다 라는 느낌으로 한 방향으로 갈 수 있을 만큼
# 깊게 탐색한다는 의미에서  깊이 우선 탐색이라는 이름이 붙었습니다.
# 갈 수 있는 한 끝까지 탐색해 리프 노드를 방문하고,
# 이전 갈림길에서 선택하지 않았던 노드를 방문하는 식으로 탐색한다.
# DFS는 스택(Stack)으로 자료구조를 대체하기만 하면 쉽게 구현가능하다.
graph_list = {1: set([3, 4]),
              2: set([3, 4, 5]),
              3: set([1, 5]),
              4: set([1]),
              5: set([2, 6]),
              6: set([3, 5])}
root_node = 1
# 라는 문제식을 DFS로 풀이한다면

def DFS_list(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
    return visited

print(DFS_list(graph_list, root_node))
# 가 된다.