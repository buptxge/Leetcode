class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sum_3 = 0
        nums.sort()
        l = len(nums)
        result = []
        for i in range(l-2):
            first = nums[i]
            if (i > 0) and (nums[i-1] == first):
                continue
            left = i + 1
            right = l - 1
            sum_2 = sum_3 - first
            while(left < right):
                current_sum = nums[left] + nums[right]
                if (current_sum == sum_2):
                    result.append([first, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while (left < right and nums[left-1] == nums[left]):
                        left += 1
                    while (left < right and nums[right+1] == nums[right]):
                        right -= 1
                elif current_sum > sum_2:
                    right -= 1
                else:
                    left += 1
        return result