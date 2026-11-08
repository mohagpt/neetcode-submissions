class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixCount = {0:1}

        res = 0 
        crtSum = 0
        for n in nums : 
            crtSum += n 
            res += prefixCount.get(crtSum-k, 0 )
            prefixCount[crtSum] = prefixCount.get(crtSum,0) + 1
            
        return res 
