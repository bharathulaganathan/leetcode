class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        tree = self.deconstruct(root)
        tree.sort()
        root_node = self.construct_binary(tree)
        return root_node

    def deconstruct(self, root):
        current = [root]
        nodes = []
        while current:
            node = current.pop(0)
            if node == None:
                continue
            nodes.append(node.val)
            current.append(node.left)
            current.append(node.right)
        return nodes

    def construct_binary(self, tree):
        if not tree:
            return None
        mid = int(len(tree)/2)
        node = TreeNode(tree[mid]) or None
        node.left = self.construct_binary(tree[:mid]) or None
        node.right = self.construct_binary(tree[mid+1:]) or None
        return node

def run(input):
    construct = construct_tree(**input)
    result = Solution().balanceBST(construct)
    return full_deconstruct(result)

def construct_tree(root):
    if not root:
        return None
    first_val = root.pop(0)
    first_node = TreeNode(val=first_val)
    current = [first_node]
    while current and root:
        node = current.pop(0)
        left = root.pop(0)
        if left is not None:
            left = TreeNode(val=left)
            current.append(left)
        node.left = left
        right = None
        if root:
            right = root.pop(0)
        if right is not None:
            right = TreeNode(val=right)
            current.append(right)
        node.right = right
    return first_node

def full_deconstruct(root):
    current = [root]
    nodes = []
    while current:
        node = current.pop(0)
        if node == None:
            nodes.append(None)
            continue
        nodes.append(node.val)
        current.append(node.left)
        current.append(node.right)
    while True:
        if nodes[-1] == None:
            nodes.pop(-1)
        else:
            break
    return nodes
