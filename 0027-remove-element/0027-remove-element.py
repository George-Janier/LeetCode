class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        f = 0
        s = 0
        while(f<len(nums)):
            if nums[f]!=val:
                nums[s]=nums[f]
                s+=1
            f+=1
        return s