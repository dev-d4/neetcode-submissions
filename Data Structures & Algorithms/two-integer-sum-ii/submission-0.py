class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i_start = 0
        i_end = len(numbers)-1
        output = []
        while len(output)==0:
            if numbers[i_start]+numbers[i_end]>target:
                i_end-=1
            elif numbers[i_start]+numbers[i_end]<target:
                i_start+=1
            else:
                output.append(i_start+1)
                output.append(i_end+1)
        return output