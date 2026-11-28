class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        sorted_nums = sorted(nums)
        len_num = len(nums)
        res = []

        for idx in range(len_num):
            i = idx + 1
            j = len_num - 1
            
            if idx > 0 and sorted_nums[idx] == sorted_nums[idx - 1]:
                continue
            
            while i < j:
                if sorted_nums[i] + sorted_nums[j] > - sorted_nums[idx]:
                    j -= 1

                elif sorted_nums[i] + sorted_nums[j] < - sorted_nums[idx]:
                    i += 1

                elif sorted_nums[i] + sorted_nums[j] == - sorted_nums[idx]:
                    res.append([sorted_nums[i], sorted_nums[j], sorted_nums[idx]])
                    i += 1
                    j -= 1

                    while i < j and sorted_nums[i] == sorted_nums[i-1]:
                        i += 1

                    while i < j and sorted_nums[j] == sorted_nums[j+1]:
                        j -= 1
        
        return res