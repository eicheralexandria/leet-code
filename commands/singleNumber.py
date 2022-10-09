class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        found = []
        for num in nums:
            if num not in found:
                found.append(num)
            else:
                found.remove(num)
        return found[0]
        