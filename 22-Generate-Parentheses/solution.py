class Solution(object):
    def find(self,left,right,s,ans):
        if (left == right) and (left == 0):
            ans.append(s)
            return
        
        if left > 0:
            self.find(left-1, right, s+'(', ans)
        
        if right > 0 and right > left:
            self.find(left, right-1, s+')', ans)
            
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        self.find(n,n,'',ans)
        return ans
        
        