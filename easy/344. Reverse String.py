class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for k in range(int(len(s)/2)):
            s[k], s[len(s)-k-1] = s[len(s)-k-1], s[k]
        return s
