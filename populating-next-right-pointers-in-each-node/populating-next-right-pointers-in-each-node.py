"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        currList, nextList = [root], []

        while currList != []:
            for i in range(len(currList)):
                if currList[i] != None:
                    if i < len(currList) - 1:
                        currList[i].next = currList[i + 1]
                    nextList.append(currList[i].left)
                    nextList.append(currList[i].right)
            currList, nextList = nextList, []
        
        return root
