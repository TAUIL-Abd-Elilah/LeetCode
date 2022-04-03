class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort() # [0,1,3,5,6] 
        h = 0
        for k in range(len(citations)):
            k = len(citations) - k - 1
            if h < citations[k]:
                h = h + 1
        return h