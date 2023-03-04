class Solution:
    def splitNum(self, num: int) -> int:
        sol = 0
        arr = list(map(int, list(str(num))))
        lenarr = len(arr)
        if lenarr % 2 == 0:
            for i in range(lenarr):
                if i % 2 == 0:
                    minelement = min(arr)
                    arr.remove(minelement)
                    sol += minelement
                else:
                    minelement = min(arr)
                    arr.remove(minelement)
                    sol += minelement
                    if i != lenarr - 1:
                        sol *= 10
        else:
            for i in range(lenarr):
                if i % 2 == 0:
                    minelement = min(arr)
                    arr.remove(minelement)
                    sol += minelement
                    if i != lenarr - 1:
                        sol *= 10
                else:
                    minelement = min(arr)
                    arr.remove(minelement)
                    sol += minelement

        return sol
        