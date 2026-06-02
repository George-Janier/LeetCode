class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        n = str(num)
        while len(n)>1:
            s = 0
            for i in n:
                s+= int(i)
            n = str(s)
        return int(n)
