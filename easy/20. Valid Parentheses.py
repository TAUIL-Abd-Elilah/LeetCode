class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for k in s:
            if k == '(' or k =='[' or k == '{':
                stack.append(k)
            else:
                if len(stack)  == 0:
                    return False
                if (k == ')' and stack[-1] == '(') or k == ']' and stack[-1] == '[' or k == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    stack.append(k)
        if len(stack) == 0:
            return True
        return False
