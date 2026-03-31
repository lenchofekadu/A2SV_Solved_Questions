# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sub(node):
            if node == None:
                return "Lencho"

            lst = [node.val, sub(node.left), sub(node.right)]

            return lst
        
        def check(node, t):
            if node == None:
                return False

            if sub(node) == t:
                return True

            return check(node.left, t) or check(node.right, t)
            
        target = sub(subRoot)
        return check(root, target)


        
            
