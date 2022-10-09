class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if nums1 == [] and nums2 == []:
            return float(0)
        elif nums1 == []:
            return self.findMedian(nums2)
        elif nums2 == []:
            return self.findMedian(nums1)
        
        else:
            merged = self.merge(nums1, nums2)
            return self.findMedian(merged)
        
    def findMedian(self, arr):
        merged_len = len(arr)
        
        if merged_len % 2 == 0:
            mid = int(merged_len / 2)
            
            a = arr[mid-1]
            b = arr[mid]
            return (a + b) / 2
        else:
            mid = int((merged_len - 1) / 2)
            return float(arr[mid])
            
    def merge(self, nums1, nums2):
        merged = []
        i = 0
        j = 0
        while True:
            a = nums1[i]
            b = nums2[j]
            if a < b:
                merged.append(a)
                i += 1
            elif a == b:
                merged.append(a)
                merged.append(b)
                i += 1
                j += 1
            else:
                merged.append(b)
                j += 1
                
            if i == len(nums1):
                merged = merged + nums2[j:]
                return merged
            elif j == len(nums2):
                merged = merged + nums1[i:]
                return merged
