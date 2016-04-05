class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        s = str(x)
        bin = False
        result = ""
        if s[0] == '-':
            bin = True
            s = s[1:]
            
        for i in range(len(s)):
            result += s[-i-1]
            
        while (result[0] == '0') and (len(result)>1):
            result = result[1:]
            
        if bin:
            result = '-'+result
        
        if (int(result)>pow(2,31)-1) or (int(result)<-pow(2,31)+1):
            return 0
        else:
            return(int(result))
    
        