class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        place = 1
        
        while (place < length):
            if (nums[place] == nums[place-1]):
                nums.pop(place)
                nums.append('X')
                length -= 1
            else :
                place += 1
        
        return length


