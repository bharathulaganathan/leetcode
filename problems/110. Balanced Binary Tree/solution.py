# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TreeConstruct:
    def construct(self, root):
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

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root:
            return self.height(root,1)
        return True

    def height(self, node, h):
        if node.left is None and node.right is None:
            if h == 1:
                return True
            return h
        left = h
        right = h
        if node.left is not None:
            left = self.height(node.left, h+1)
            if not left:
                return False
        if node.right is not None:
            right = self.height(node.right, h+1)
            if not right:
                return False
        if abs(left - right) > 1:
            return False
        if h == 1:
            return True
        return max(left, right)

def run(input):
    solution = Solution()
    tree_root = TreeConstruct().construct(**input)
    return solution.isBalanced(tree_root)
