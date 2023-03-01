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
    def connect(self, root: 'Node') -> 'Node':
        currList, nextList = [root], []

        while currList != []:
            filterCurrList = list(filter(lambda x: x != None, currList))
            for i in range(len(filterCurrList)):
                if i < len(filterCurrList) - 1:
                    filterCurrList[i].next = filterCurrList[i + 1]
                nextList.append(filterCurrList[i].left)
                nextList.append(filterCurrList[i].right)
            currList, nextList = nextList, []
        
        return root
