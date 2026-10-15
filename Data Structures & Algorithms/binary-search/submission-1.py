class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_serach(0,len(nums)-1,nums,target)
        
    
    def binary_serach(self, l, r, nums, target):
        if l > r:
            return -1

        mid = l + (r - l) // 2
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            return self.binary_serach(mid+1,r,nums,target)
        else:
            return self.binary_serach(l, mid-1, nums, target)

        