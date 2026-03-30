class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0 
        stack = [] #pair : (index, height )

        for i, h in enumerate(heights):
            head = i 
            while stack and heights[i] < stack[-1][1]:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                head = index

            stack.append((head, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))


        return maxArea