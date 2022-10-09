class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ""
        str_lens = [len(s) for s in strs]
        min_len = min(str_lens)
        longestPrefix = ""
        
        for n in range(min_len):
            prefix = strs[0][:n+1]
            for s in range(1, len(strs)):
                if strs[s][:n+1] != prefix:
                    return longestPrefix
            longestPrefix = prefix
        return longestPrefix