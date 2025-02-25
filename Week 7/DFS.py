class Node:
    def __init__(self, key):
        self.key = key
        self.children = []

def depth_limited_search(node, target, depth):
    if node is None:
        return False
    if node.key == target:
        return True
    if depth <= 0:
        return False
    for child in node.children:
        if depth_limited_search(child, target, depth - 1):
            return True
    return False

def iterative_deepening_dfs(root, target):
    depth = 0
    while True:
        if depth_limited_search(root, target, depth):
            return True
        depth += 1

root = Node(1)
root.children = [Node(2), Node(3), Node(4)]
root.children[0].children = [Node(5), Node(6)]
root.children[2].children = [Node(7), Node(8)]

target = 7
if iterative_deepening_dfs(root, target):
    print(f"Target {target} found in the tree.")
else:
    print(f"Target {target} not found in the tree.")