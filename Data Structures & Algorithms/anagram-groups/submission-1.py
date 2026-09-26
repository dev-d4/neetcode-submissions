class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = {"".join(list(sorted(s))):[] for s in strs}
        for s in strs:
            str_dict["".join(list(sorted(s)))].append(s)

        return [v for k,v in str_dict.items()]