from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        total_vol = 0

        max_height = max(height)
        max_index = height.index(max_height)

        # Left -> max
        height_before = 0
        index_before = 0
        vol_remove = 0

        for i, h in enumerate(height[:max_index + 1]):
            if h > 0 and h >= height_before:
                width = i - index_before - 1
                water_height = min(h, height_before)

                vol = width * water_height
                total_vol += vol - vol_remove

                vol_remove = 0
                index_before = i
                height_before = h

            elif h > 0 and h < height_before:
                vol_remove += h

        # Right -> max
        reversed_heights = height[max_index:][::-1]

        height_before = 0
        index_before = 0
        vol_remove = 0

        for i, h in enumerate(reversed_heights):
            if h > 0 and h >= height_before:
                width = i - index_before - 1
                water_height = min(h, height_before)

                vol = width * water_height
                total_vol += vol - vol_remove

                vol_remove = 0
                index_before = i
                height_before = h

            elif h > 0 and h < height_before:
                vol_remove += h

        return total_vol