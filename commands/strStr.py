class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
            
        place = needle[0]
            
        for i in range(len(haystack)):
            if haystack[i] == place:
                if haystack[i:i+len(needle)] == needle:
                    return i
                    
        return -1