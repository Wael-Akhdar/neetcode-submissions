class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        len_num = len(numbers)
        res = []
        for i in range(len_num):
            for j in range(i+1, len_num-1):
                if numbers[i] + numbers[j] == target:
                    res.append(i+1)
                    res.append(j+1)
                    return res