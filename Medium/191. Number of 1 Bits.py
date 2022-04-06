############### Video where i explain the solution https://www.youtube.com/watch?v=lcP25-MzfMA
############### Problem link https://leetcode.com/problems/number-of-1-bits/
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        c = 0
        while n > 0:
            if n & 1 ==1 :
                c += 1
            n = n >> 1
        return c
