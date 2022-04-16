class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = ''.join(filter(str.isalnum, s)).lower()
        if s == '':
            return True
        for k in range(int(len(s)/2)):
            if s[k] != s[len(s)-k-1]:
                return False
        return True
