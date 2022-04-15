############### rob Link https://leetcode.com/problems/unique-paths/
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        out = [[0] * m] *n
        for k in range(m):
            out[0][k] = 1
        for k in range(n):
            out[k][0] = 1
        for i in range(1,n ):
            for j in range(1,m):
                out[i][j] = out[i][j-1] + out[i-1][j]
        return out[n-1][m-1]
