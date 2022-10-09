class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = sum(nums)
        
        for i in range(len(nums)):

            for j in range(i+1, len(nums)+1):
                print(nums[i:j])
                thisSum = sum(nums[i:j])
                if thisSum > maxSum:
                    maxSum = thisSum
        return maxSum

sol = Solution()
nums = [1,2,-1]
#nums = [5,4,-1,7,8]
#nums = [-2, 1]
#nums = [-2,1,-3,4,-1,2,1,-5,4]
print(sol.maxSubArray(nums))