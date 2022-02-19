# BFS의 알고리즘의 핵심은 큐(QUEUE) 자료구조를 사용하는 것인데요.
# 노드를 방문하면서 인접한 노드 중 방문하지 않았던 노드의 정보만 큐에 넣어 먼저 큐에 들어있던
# 노드부터 방문하면 되는 것이다. 물론 큐를 사용하지 않아도 구현이 가능하다.
# queue를 list타입을 사용해 자료를 입력할 때 list.append()
# 자료를 출력할 때 list.pop()
# 하지만 list.pop()은 비효율 적인 코드가 만들어지니
# collections라이브러리에 deque를 사용하면 시간절약이 된다.
# 또한 인접 노드 중 방문하지 않았던 노드를 queue에 넣을 때는 파이썬 데이터 타입 중
# set을 사용하면 아주 쉽게 구현할 수 있다.

graph_list = {1: set([3, 4]),
              2: set([3, 4, 5]),
              3: set([1, 5]),
              4: set([1]),
              5: set([2, 6]),
              6: set([3, 5])}
root_node = 1
# 을 BFS로 탐색한다면,
from collections import deque

def BFS_list(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    return visited

print(BFS_list(graph_list, root_node))
# 이렇게 구현하면 된다.