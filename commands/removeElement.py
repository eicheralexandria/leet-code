class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        place = 0
        while (place < length):
            if (nums[place] == val):
                nums.pop(place)
                nums.append('X')
                length -= 1
            else:
                place += 1
        return length