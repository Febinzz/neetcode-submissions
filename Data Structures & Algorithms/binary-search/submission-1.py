class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        flag=0
        high=len(nums)-1
        while(low<=high):
            mid=(low+high)//2
            print(mid)
            if nums[mid]==target:
                flag=1
                break
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        if flag==1:
            return mid
        else:
            return -1



        