class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        n = len(height)
        for i in range(n):
            yi = height[i]
            for j in range(n):
                if i != j:
                    yj = height[j]
                    h = min(yi, yj)
                    l = abs(i-j)
                    area = h * l
                    if area > maxArea:
                        maxArea = area
        return maxArea
        
sol = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(sol.maxArea(height))