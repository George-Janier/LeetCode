class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        s = set(word)
        count = 0

        for ch in s:
            if ch.islower() and ch.upper() in s:
                count += 1

        return count