class Solution(object):
    def concatWithReverse(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = nums + nums[::-1]
        return nums