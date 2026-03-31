# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        def find(node):
            if node == None:
                return 0
            if node.left == None:
                return 1 + find(node.right)
            if node.right == None:
                return 1 + find(node.left)
            
            return 1 + min(find(node.left), find(node.right))

        return find(root)