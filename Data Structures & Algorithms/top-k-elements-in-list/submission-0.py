class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        most_freq_dict = {k:0 for k in set(nums)}
        for num in nums:
            most_freq_dict[num] += 1

        most_freq_dict_sorted = list(dict(sorted(most_freq_dict.items(), key=lambda x:-x[1])))
        print(most_freq_dict_sorted)
        return most_freq_dict_sorted[:k]