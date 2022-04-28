class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        def helper(i,j):
            if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j] == 1:
                c = 1
                grid[i][j] = 0
                c += helper(i+1,j)
                c += helper(i-1,j)
                c += helper(i,j+1)
                c += helper(i,j-1)
            else:
                c = 0
            return c
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ans = max(ans, helper(i,j))
        return ans
