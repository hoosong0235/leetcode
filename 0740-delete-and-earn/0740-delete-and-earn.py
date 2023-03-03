class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counts = [nums.count(i) for i in range(max(nums)+ 1)]
        dp = [0 for _ in range(max(nums) + 1)]
        dp[0] = 0
        dp[1] = counts[1]

        for i in range(2, max(nums) + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + counts[i] * i)

        return dp[max(nums)]
        