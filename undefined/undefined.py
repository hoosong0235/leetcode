class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # 1 2 3   4 3 2   1 2 3   4 3 2
        return (time % (n - 1) + 1) if ((time // (n - 1)) % 2 == 0) else (n - time % (n - 1))