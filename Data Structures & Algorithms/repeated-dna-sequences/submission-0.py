class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        myCrtMap = {}

        if len(s) <= 10 :
            return []


        for i in range (10, len(s)+1) : 
            subStr = s[i-10: i]
            if subStr in  myCrtMap : 
                if not myCrtMap[subStr] : 
                    myCrtMap[subStr].append(subStr)
            else : 
                myCrtMap[subStr] = []

        return [subStr[0] for subStr in myCrtMap.values() if subStr]
