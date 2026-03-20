# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        
        def dmr(node, parent, grandpa):
            if node == None:
                return 0 
   
            current = node.val if grandpa and grandpa % 2 == 0  else 0

            return current + dmr(node.left, node.val, parent) + dmr(node.right, node.val, parent)


        return dmr(root, None, None)