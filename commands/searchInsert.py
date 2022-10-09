class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.search(nums, target, 0)
        
    def search(self, nums, target, start):
        if len(nums) == 1:
            return start if target <= nums[0] else start + 1
        mid = len(nums) // 2
        if target == nums[mid]:
            return start + mid
        elif target < nums[mid]:
            return self.search(nums[:mid], target, start)
        else:
            return self.search(nums[mid:], target, start + mid)