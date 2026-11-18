class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hash_map = {}

        for elt in nums:
            
            if not hash_map.get(elt,0):
                hash_map[elt] = 1
            else:
                hash_map[elt] += 1
        
        return sorted(hash_map, key=lambda a : hash_map[a], reverse=True)[:k]
