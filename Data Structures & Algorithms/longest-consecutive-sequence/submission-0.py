class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        my_set = set(nums)
        curr = 0
        max_len = 0
        for i in nums:
            if not i-1 in my_set:
                curr = i
                cpt = 1
                while curr+1 in my_set:
                    curr = curr+1
                    cpt += 1
                max_len = max(cpt, max_len)
        return max_len





