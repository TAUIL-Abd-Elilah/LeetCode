############## Prob link : https://leetcode.com/problems/first-unique-character-in-a-string/
class Solution:
    def firstUniqChar(self, s: str) -> int:
        r = {}
        for k in s :
            if k in r :
                r[k] = r[k] + 1
            else:
                r[k] = 0
                
        for k in range(len(s)):
            if r[s[k]] == 0 :
                return k
        return -1 
