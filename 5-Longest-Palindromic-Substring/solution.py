class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        if s == "":
            return ""
        
        max_string = ""
        max_length = -1
            
        n = len(s)
        dp = [[1 for i in xrange(n)] for j in xrange(n)]
        for i in xrange(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 2
                
        for l in xrange(2,n):
            for i in xrange(n):
                if i+l>=n:
                    break

            if (s[i] == s[i+l]):
                dp[i][i+l] = dp[i+1][i+l-1] + 2
            else:
                dp[i][i+l] = dp[i+1][i+l-1]
            if dp[i][i+l]>max_length:
                max_length = dp[i][i+l]
                max_string = s[i:i+l+1]
                
        return max_string
        