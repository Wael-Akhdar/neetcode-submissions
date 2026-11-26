class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        len_num = len(numbers)
        res = []
        i = 0
        j = len_num - 1
        
        while i < j:

            if numbers[i] + numbers[j] > target:
                j -= 1

            elif numbers[i] + numbers[j] < target:
                i += 1

            elif numbers[i] + numbers[j] == target:
                res.append(i+1)
                res.append(j+1)
                return res