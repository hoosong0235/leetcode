# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        solution = list()
        if root != None:
            solution += self.postorderTraversal(root.left)
            solution += self.postorderTraversal(root.right)
            solution.append(root.val)
        return solution