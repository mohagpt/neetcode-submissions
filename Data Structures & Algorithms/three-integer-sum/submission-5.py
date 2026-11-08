class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        res = []

        for i,a in enumerate(nums) : 
            if a > 0:
                break
            if 0 < i < len(nums) and a == nums[i-1] : 
                continue
            l, r = i+1, len(nums) - 1 
            
            while l < r : 
                b , c = nums[l], nums[r] 
                if a + b + c == 0 : 
                    res.append([a,b,c])
                    l+=1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif a + b + c < 0 : 
                    l += 1
                else : 
                    r -= 1

        return res
        
        