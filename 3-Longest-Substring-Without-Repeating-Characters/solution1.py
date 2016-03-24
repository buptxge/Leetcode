class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        
        ans = [1]*len(s)
        lastpos[s[0]] = 0
        result = 1
        
        for i in range(1,len(s)):
            if s[i] not in lastpos:
                ans[i] = ans[i-1]
            else:
                ans[i] = min(i-lastpos[s[i]],ans[i-1])
            is ans[i]>result:
                result = ans[i]
        return result