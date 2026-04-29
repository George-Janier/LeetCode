class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLen = 0
        currentL = 0
        occured = set()
        left = 0  # This will keep track of the start of the sliding window
        
        for i in range(len(s)):
            # If the current character is in the set, slide the left pointer
            while s[i] in occured:
                occured.remove(s[left])
                left += 1
                currentL -= 1  # Decrease the length of the current substring
            
            # Add the current character to the set and increase the length of the substring
            occured.add(s[i])
            currentL += 1
            
            # Update the max length found so far
            maxLen = max(maxLen, currentL)
        
        return maxLen
