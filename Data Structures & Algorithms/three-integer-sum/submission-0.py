class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1] :
                continue
            
            l, r = i+1, len(nums) - 1
            while r > l : 
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0 :
                    r -= 1
                elif 0 > threeSum : 
                    l += 1
                else :
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and r > l :
                        l += 1


        return res

        