class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s1 = ''
        for e in s:
            if e.isalnum():
                s1 = s1 + e.lower()
        i=0
        j=len(s1)-1
        while(i<j):
            if s1[i]!=s1[j]:
                return False
            i+=1
            j-=1
        return True