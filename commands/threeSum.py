class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sols = []
        numsLen = len(nums)
        
        [sols.append(sorted([nums[i], nums[j],  0-(nums[i] + nums[j])])) for i in range(numsLen) for j in range(i+1, numsLen) if (0-(nums[i] + nums[j]) in nums[j+1:]) and (sorted([nums[i], nums[j],  0-(nums[i] + nums[j])]) not in sols)]
                        
        return sols
        
sol = Solution()
nums = [-1,0,1,2,-1,-4]
#nums = []
#nums = [0]

print(sol.threeSum(nums))