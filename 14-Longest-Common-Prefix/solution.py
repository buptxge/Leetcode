class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        if len(strs) == 1:
            return strs[0]

        longest_s = strs[0]
        for s in strs:
            if len(s) > len(longest_s):
                longest_s = s

        for i in range(len(longest_s)):
            prefix = longest_s[:i+1]
            for s in strs:
                if not s.startswith(prefix):
                    return longest_s[:i]

        return longest_s
