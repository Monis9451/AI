from collections import deque

def shortestPathMaze(grid):
    if not grid or grid[0][0] == 1 or grid[-1][-1] == 1:
        return -1 

    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(0, 0, 1)])
    visited = set((0, 0))

    while queue:
        r, c, steps = queue.popleft()

        if (r, c) == (rows - 1, cols - 1):
            return steps

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                queue.append((nr, nc, steps + 1))
                visited.add((nr, nc))

    return -1  

maze = [
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 0],
    [1, 1, 0, 0]
]

print("Shortest Path Length:", shortestPathMaze(maze))
