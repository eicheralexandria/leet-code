class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = 0
        longestSubstring = 0
        substring = ""
        finalSubstring = ""
        while n < len(s):
            letter = s[n]
            if letter in substring:
                index = substring.index(letter)
                print("letter " + letter + " in substring at index " + str(index))
                substring = substring[index+1:]
                
                
            substring += letter
                
            if len(substring) > longestSubstring:
                longestSubstring = len(substring)
                finalSubstring = substring
            n += 1
        print(finalSubstring)
        return longestSubstring
        
sol = Solution()
s = "pwwkew"
sol.lengthOfLongestSubstring(s)
