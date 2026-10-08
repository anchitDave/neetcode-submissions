class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()
        for i in range(len(nums) - 2):
            ptr1 = i + 1
            ptr2 = len(nums) - 1

            while ptr1 < ptr2:
                s = nums[i] + nums[ptr1] + nums[ptr2]

                if s == 0:
                    ans.add((nums[i], nums[ptr1], nums[ptr2]))
                    ptr1 += 1
                    ptr2 -= 1
                    while nums[ptr1] == nums[ptr1 - 1] and ptr1 < ptr2:
                        ptr1 += 1
                
                if s > 0:
                    ptr2 -= 1
                
                if s < 0:
                    ptr1 += 1
        
        return [list(t) for t in ans]
        