class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l, r, o = [1], [1], []
        if len(nums) == 0:
            return 0
        else:
            for k in range(len(nums)):
                if k != len(nums)-1:
                    l.append(l[-1]* nums[k])
                k = len(nums) - k - 1
                if k!=0:
                    r.append(r[-1]*nums[k])
            for k in range(len(nums)):
                o.append(l[k]*r[len(nums)-1 -k])
            return o
