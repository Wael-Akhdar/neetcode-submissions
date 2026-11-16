class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        len_nums = len(nums)

        for i in range (len_nums):
            for j in range (i + 1, len_nums):
                if nums[i] + nums[j] == target:
                    res.append(i)
                    res.append(j)
                    return res

        return res