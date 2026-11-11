class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        finalDoc = []
        
        currentStr = []
        crtLen = 0 
        for w in words : 
            if crtLen + len(currentStr) - 1 + len(w) < maxWidth : 
                crtLen += len(w)
                currentStr.append(w)
                continue
            if len(currentStr) == 1 : 
                finalDoc.append(currentStr[0].ljust(maxWidth))
            else : 
                remainingSpace = maxWidth - (crtLen + len(currentStr) - 1) 
                spaceBtwnWords = 1 + remainingSpace // (len(currentStr) - 1)
                remainingSpace %= (len(currentStr) - 1)

                finalStr = (" " * (spaceBtwnWords + 1)).join(currentStr[:remainingSpace+1])
                finalStr += (" " * spaceBtwnWords) 
                finalStr += (" " * spaceBtwnWords).join(currentStr[remainingSpace+1:])
                
                finalDoc.append(finalStr)
            crtLen = len(w)
            currentStr = [w]

        if currentStr : 
            finalDoc.append(" ".join(currentStr).ljust(maxWidth))

        return finalDoc