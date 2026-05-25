class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxV = 0
        l = 0
        r = len(height)-1
        while l < r :
            vol = min(height[l], height[r]) * (r-l)
            maxV = max(maxV, vol)
            if height[l]<height[r]:
                l+=1
            else :
                r-=1
        return maxV