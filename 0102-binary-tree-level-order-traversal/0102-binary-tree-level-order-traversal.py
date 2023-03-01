# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, rootList):
        currList, nextList = list(), list()

        for root in rootList:
            if root != None:
                currList.append(root.val)
                nextList.append(root.left)
                nextList.append(root.right)

        return currList, nextList

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        solution = list()

        currList, nextList = self.solve([root])
        while nextList != list():
            if currList != list():
                solution.append(currList)
            currList, nextList = self.solve(nextList)
        
        return solution
