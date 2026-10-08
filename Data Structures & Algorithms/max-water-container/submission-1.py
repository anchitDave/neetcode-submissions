class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ptr1, ptr2 = 0, len(heights) - 1
        maxA = min(heights[0], heights[-1])*(ptr2 - ptr1)
        while ptr1 < ptr2:
            if heights[ptr1] <= heights[ptr2]:
                ptr1 += 1
            else:
                ptr2 -= 1
            maxA = max(min(heights[ptr1], heights[ptr2])*(ptr2 - ptr1), maxA)
        
        return maxA

        