class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        def div(times, val):
            if val + val <= dividend:
                temp_val, temp_times= div(times + times, val + val)
                while temp_val + val <= dividend:
                    temp_val += val
                    temp_times += times
                return temp_val, temp_times
            else:
                return val, times
                
        if divisor == 0:
            return -1
        flag = 0
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            flag = 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        if divisor <= dividend:
            temp1,temp2 = div(1,divisor)
            if flag:
                temp2 = 0 - temp2
            return min(max(-2147483648, temp2), 2147483647)
        else:
            return 0