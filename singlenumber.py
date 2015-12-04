#Given an array of integers, every element appears twice except for one. Find that single one.

#Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

#应该还有其他比较复杂的解法，以后解决

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        singlenumber = 0
        for i in nums:
            singlenumber = i ^ singlenumber
        return singlenumber  
        