# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, first, second):
        if first == None and second == None:
            return True
        elif first == None or second == None:
            return False
        elif first.val != second.val:
            return False
        else:
            return self.solve(first.left, second.right) and self.solve(first.right, second.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.solve(root.left, root.right)