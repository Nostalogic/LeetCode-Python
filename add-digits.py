

# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

#For example:

#Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it. class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        if num == 0:
            num = 0
        elif num%9 == 0:
            num = 9
        else:
            num = num % 9
        print num