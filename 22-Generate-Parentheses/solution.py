class Solution(object):
    def find(left,right,s,ans):
        if left == right and left == 0：
            ans.append(s)
            return
        
        if left > 0:
            find(left-1, right, s+'(', ans)
        
        if right > 0: and right > left:
            find(left, right+1, s+')', ans)
            
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        find(3,3,'',ans)
        return ans
        
        