class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        len_nums = len(nums)

        res = []

        cpt = 1
        for i in range (len_nums):
            
            res.append(cpt)
            cpt *= nums[i]

        cpt = 1
        for i in range ((len_nums) - 1, -1, -1):
            res[i] *= cpt
            cpt *= nums[i]

        return res





        