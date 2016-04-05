class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        if (numRows == 1):
            return s
        
        result = [""]*numRows
        now_row = 0
        index = 0
        direction = 1 #1：down -1:up
        while (index <= len(s)-1):
            result[now_row]+= s[index]
            index += 1 
            if (now_row == numRows-1):
                now_row = numRows-2
                direction = -1
            elif (now_row == 0):
                now_row = 1
                direction = 1
            else:
                now_row += direction
            
        return "".join(result)
                
            
            
