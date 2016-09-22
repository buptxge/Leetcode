class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        j = len(nums) - 1
        while True:
            while i<j and nums[j] == val:
                j -= 1
                
            if nums[i] == val:
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
                j -= 1
            else:
                i += 1
                
            if i > j:
                break
            
        return len(nums) - j
            