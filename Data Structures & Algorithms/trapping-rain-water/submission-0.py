class Solution:
    def trap(self, height: List[int]) -> int:
        size = len(height)
        left_max = [0] * size
        right_max = [0] * size

        for i in range(size):
            if i == 0 or height[i] >= left_max[i-1]:
                left_max[i] = height[i]
            else:
                left_max[i] = left_max[i-1]

        for i in range(size-1, -1, -1):
            if i == size-1 or height[i] >= right_max[i+1]:
                right_max[i] = height[i]
            else:
                right_max[i] = right_max[i+1]
        
        water_size = 0
        for i in range(1, size):
            water_size_cur = min(right_max[i], left_max[i]) - height[i]
            
            water_size += water_size_cur
        
        return water_size