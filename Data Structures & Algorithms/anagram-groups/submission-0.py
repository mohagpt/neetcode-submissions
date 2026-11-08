class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}

        for s in strs :
            key = "".join(sorted(s))
            val = dictionary.get(key)
            if val == None : 
                dictionary[key] = [s]
            else : 
                val.append(s)
                dictionary[key] = val
        
        return list(dictionary.values())


        