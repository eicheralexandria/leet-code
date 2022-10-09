class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sets = []
        anagrams = {}
        for s in strs:
            sortedSetS = sorted(tuple(s))
            if sortedSetS in sets:
                index = sets.index(sortedSetS)
                anagrams[index].append(s)
            else:
                sets.append(sortedSetS)
                index = sets.index(sortedSetS)
                anagrams[index] = [s]
        return list(anagrams.values())