class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        y=(len(nums1)-1)//2
        if len(nums1)%2 !=0:
            return(nums1[y])
        else:
            return((nums1[y]+nums1[y+1])/2)
            
        
        