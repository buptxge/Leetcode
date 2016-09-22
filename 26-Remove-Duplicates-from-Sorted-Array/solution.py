class Solution(object):
       def removeDuplicates(self, nums):
        i=1
        j=1
        a=len(nums)
        while i<a:
            if nums[i]>nums[i-1]:
                nums[j]=nums[i]
                j+=1
            i+=1
        return len(set(nums))