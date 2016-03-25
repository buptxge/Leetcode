class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_length = 0
        max_str = ""
        
        for i in range(len(s)):
            left = right = i
            tmp_str = s[i]
            while (left>0) and (right<len(s)-1):
                left -= 1
                right += 1
                if s[left] == s[right]:
                    tmp_str = s[left] + tmp_str + s[right]
                else:
                    break
            if len(tmp_str)>max_length:
                max_length = len(tmp_str)
                max_str = tmp_str
        
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                left = i
                right = i+1
                tmp_str = s[i]+s[i+1]
                while (left > 0) and (right<len(s)-1):
                    left -= 1
                    right += 1
                    if s[left] == s[right]:
                        tmp_str = s[left]+tmp_str+s[right]
                    else:
                        break
                if len(tmp_str) > max_length:
                    max_length = len(tmp_str)
                    max_str = tmp_str
                
        return max_str
                    