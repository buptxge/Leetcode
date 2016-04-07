import math

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x<0):
            return False
        
        power = int(math.log(x,10))
        while(power>0):
            if (x/pow(10,power)) != (x % 10):
                return False
            x -= (x/pow(10,power)) * pow(10,power)
            x = x / 10
            power -= 2
            
        return True
                