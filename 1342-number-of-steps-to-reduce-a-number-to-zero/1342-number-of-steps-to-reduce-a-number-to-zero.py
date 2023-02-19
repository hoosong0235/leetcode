class Solution:
    def numberOfSteps(self, num: int) -> int:
        sol = 0
        while num:
            if num % 2:
                num -= 1
            else:
                num /= 2
            sol += 1
        return sol