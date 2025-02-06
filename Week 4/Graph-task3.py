from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrderTraversal(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        levelSize = len(queue)
        currentLevel = []
        
        for _ in range(levelSize):
            node = queue.popleft()
            currentLevel.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(currentLevel)
    
    return result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

output = levelOrderTraversal(root)
print("Level order traversal:", output)
