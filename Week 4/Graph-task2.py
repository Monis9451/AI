from collections import deque

def bfs(graph, start, goal):
    queue = deque([start])
    visited = set()
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=' ')

        if node == goal:
            print("\nGoal node reached!")
            return

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
graph = {
    'A': ['B', 'F', 'D', 'E'],
    'B': ['K', 'J'],
    'F': [],
    'D': ['G'],
    'E': ['C', 'H', 'I'],
    'K': ['N', 'M'],
    'J': [],
    'G': [],
    'C': [],
    'H': [],
    'I': ['L'],
    'N': [],
    'M': [],
    'L': []
}

bfs(graph, 'A', 'G')
