# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        solution = list()
        if root != None:
            solution += self.inorderTraversal(root.left)
            solution.append(root.val)
            solution += self.inorderTraversal(root.right)
        return solution