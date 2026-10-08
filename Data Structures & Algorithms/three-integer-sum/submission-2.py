class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            ptr1 = i + 1
            ptr2 = len(nums) - 1

            while ptr1 < ptr2:
                s = nums[i] + nums[ptr1] + nums[ptr2]

                if s == 0:
                    ans.append([nums[i], nums[ptr1], nums[ptr2]])
                    ptr1 += 1
                    ptr2 -= 1
                    while nums[ptr1] == nums[ptr1 - 1] and ptr1 < ptr2:
                        ptr1 += 1
                
                if s > 0:
                    ptr2 -= 1
                
                if s < 0:
                    ptr1 += 1
        
        return ans
        