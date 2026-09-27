class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_sorted = sorted(set(nums))
        j = 1
        largest_j = 0

        for i,num in enumerate(nums_sorted):
            if i == 0:
                largest_j = j
                continue
            if num-nums_sorted[i-1]==1:
                j+=1
            else:
                j = 1

            if j>largest_j:
                largest_j = j

        return largest_j