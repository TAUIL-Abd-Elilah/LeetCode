############### Video solution explained https://www.youtube.com/watch?v=oKrCWtoN9Kw
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = {}
        t = -1
        h,r = 0,0
        for h in range(len(s)):
            if s[h] in letters :
                t = max(t, letters[s[h]])
            letters[s[h]] = h
            r = max(r, h-t)
        return r