# Prob link : https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def helper(elem):
            return elem[0]
        intervals.sort(key = helper)
        res = []
        for k in intervals:
            if not res or res[-1][1] < k[0]:
                res.append(k)
            else:
                res[-1][1] = max(res[-1][1], k[1])
        return res
