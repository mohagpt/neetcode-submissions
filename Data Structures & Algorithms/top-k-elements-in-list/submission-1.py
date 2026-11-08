class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        fMap = {}
        for num in nums :
            fMap[num] = fMap.get(num, 0) + 1

        arr = []
        for num, cnt in fMap.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
 
