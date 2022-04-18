class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(start):
            if start == len(nums) -1:
                res.append(nums.copy())
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                helper(start +1)
                nums[start], nums[i] = nums[i], nums[start]
        helper(0)
        return res
