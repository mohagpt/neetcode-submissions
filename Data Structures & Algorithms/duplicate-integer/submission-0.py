class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        dictionnary = {}
        for i in range(len(nums)):
            crt = dictionnary.get(nums[i])
            if crt == None :
                dictionnary[nums[i]] = 1
            else : 
                return True
        return False

        