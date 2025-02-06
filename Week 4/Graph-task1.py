from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            queue.extend([node for node in graph[vertex] if node not in visited])

graph = {
    0: [1, 4],
    1: [0, 3, 4, 2],
    2: [1, 3],
    3: [1, 2, 4],
    4: [0, 1, 3]
}

bfs(graph, 0)
