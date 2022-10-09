class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(ch for ch in s if ch.isalnum())
        s = s.lower()
        reverse = s[::-1]
        return s == reverse
            
        