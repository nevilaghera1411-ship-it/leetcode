class Solution(object):
    def largestRectangleArea(self, heights):
        stack = []  # will store indices
        max_area = 0
        heights.append(0)  # add a sentinel to pop all remaining bars
        
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                
                # width calculation
                if not stack:
                    w = i
                else:
                    w = i - stack[-1] - 1
                
                max_area = max(max_area, h * w)
            
            stack.append(i)
        
        return max_area