class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_nums = set()
        duplicate_bool = False
        for num in nums:
            if num in seen_nums:
                duplicate_bool = True
                break
            seen_nums.add(num)

        return duplicate_bool