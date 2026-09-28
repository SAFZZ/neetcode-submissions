class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        n=len(heights)
        left = 0
        right = n-1
        while left<right:
            width = right - left
            tall = min(heights[left],heights[right])
            area = width * tall
            max_area = max(max_area,area)
            if heights[left]<heights[right]:
                left +=1
            else:
                right -= 1

        return max_area
            
        