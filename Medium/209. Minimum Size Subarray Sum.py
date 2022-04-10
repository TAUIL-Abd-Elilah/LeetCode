class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        r = float('inf')
        s,p0,p1 = 0,0,0
        for p0 in range(len(nums)):
            s = s + nums[p0]
            while s >= target:
                r = min(r, p0 - p1 + 1)
                s = s - nums[p1]
                p1 = p1 + 1
        if r == float('inf'):
            return 0
        return r
