## prob link : https://leetcode.com/problems/perfect-squares/

class Solution:
    def numSquares(self, n: int) -> int:
        sq =[]
        i = 1
        out = [n+1] * (n+1)
        out[0] = 0
        while i * i <=n:
            sq.append(i*i)
            i = i+1
        for k in range(1, n+1):
            for s in sq:
                if k+s>=0:
                    out[k] = min(out[k], out[k-s] +1)
        return out[-1]
