class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = int(''.join(map(str,digits)))
        i+=1
        return list(map(int, str(i)))