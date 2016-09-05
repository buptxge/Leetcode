class Solution(object):
    def find(self, digits, now_s, ans, dic):
        if len(digits) == 0:
            ans.append(now_s)
            return
        
        for ch in dic[digits[0]]:
            self.find(digits[1:], now_s+ch, ans, dic)
    
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {
            '1':"*",
            '2':"abc",
            '3':"def",
            '4':"ghi",
            '5':"jkl",
            '6':"mno",
            '7':"pqrs",
            '8':"tuv",
            '9':"wxyz",
            '0':" "
        }
        
        ans = []
        now_s = ""
        if len(digits) > 0:
            self.find(digits,now_s,ans,dic)
            
        return ans
        