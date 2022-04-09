'''
Runtime: 32 ms, faster than 98.84% of Python3 online submissions for Largest Number.
Memory Usage: 13.9 MB, less than 24.45% of Python3 online submissions for Largest Number.
ProbLink : https://leetcode.com/problems/largest-number/submissions/
'''
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        
        def helper(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1
            
        nums = sorted(nums, key = cmp_to_key(helper))

        
        string = "".join(nums)
        if int(string)  > 0 :
            return string
        return'0'
    
