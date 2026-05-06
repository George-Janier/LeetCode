class Solution(object):
    def maxRotateFunction(self, nums):
        n = len(nums)
        total = sum(nums)
        
        f = sum(i * num for i, num in enumerate(nums))
        m = f
        
        for k in range(1, n):
            f = f + total - n * nums[-k]
            m = max(m, f)
        
        return m