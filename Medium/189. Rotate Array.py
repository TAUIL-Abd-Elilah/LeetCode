class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if len(nums) == 1 : return nums
        else:
            save = []
            for i in range(len(nums)):
                if (-k + i) <0:
                    save.append(nums[i])
                    nums[i] = nums[i-k]
                else:
                    save.append(nums[i])
                    nums[i] = save[i-k]
