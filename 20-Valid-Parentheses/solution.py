class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        
        for ch in s:
            if ch in ['(','[','{']:
                stack.append(ch)
            else:
                if not s:
                    return False
                pop_ch = stack.pop()
                if (ch == ')' and pop_ch != '(') or (ch == ']' and pop_ch != '[') or (ch == '{' and pop_ch != '}'):
                    return False
                    
        if not stack:
            return True
        else:
            return False