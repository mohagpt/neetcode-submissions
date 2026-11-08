class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        crtSum = 0 
        for num in nums : 
            crtSum += num

        if crtSum % 2 != 0 :
            return False
        
        target = crtSum // 2

        subsetSum = [False] * (target + 1)
        subsetSum[0] = True

        
        for num in nums :
            for need in range(target, num - 1, -1):
                subsetSum[need] = subsetSum[need] or subsetSum[need - num]

        
        return subsetSum[target]

