########## Prob link : https://leetcode.com/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1 :
            return 1
        first, second = 1,2
        for i in range(3, n+1):
            third = second + first
            first = second 
            second = third
        return second
        
