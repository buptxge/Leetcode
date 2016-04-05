class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if re.match("[ ]*[-+]?\d+", str):
            r = re.search("(-?\d+)", str);
            
        if r:
            return max(-2147483648, min(2147483647, int(r.group(1))))
          
        return 0
        