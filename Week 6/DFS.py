
# Task 1: Implement Depth First Search using stack
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def dfs_using_stack(root):
    if root is None:
        return []
    
    stack = [root]
    result = []
    
    while stack:
        node = stack.pop()
        result.append(node.value)
        
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return result

# Task 2: Travesals
def pre_order_traversal(root):
    if root is None:
        return []
    
    result = [root.value]
    result += pre_order_traversal(root.left)
    result += pre_order_traversal(root.right)
    
    return result

def post_order_traversal(root):
    if root is None:
        return []
    
    result = post_order_traversal(root.left)
    result += post_order_traversal(root.right)
    result.append(root.value)
    
    return result

def in_order_traversal(root):
    if root is None:
        return []
    
    result = in_order_traversal(root.left)
    result.append(root.value)
    result += in_order_traversal(root.right)
    
    return result
