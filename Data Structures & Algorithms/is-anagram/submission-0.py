class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list_sorted = sorted(list(s))
        t_list_sorted = sorted(list(t))

        return s_list_sorted == t_list_sorted
        