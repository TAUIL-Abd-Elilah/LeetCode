# Prob link :https://leetcode.com/problems/maximum-subarray/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) ==  0 :
            return 0
        else:
            m = nums[0]
            s = 0
            for k in nums:
                if k + s < 0:
                    s = 0
                    m = max(m, k)
                else:
                    s += k
                    m = max(m, s)
            return m
