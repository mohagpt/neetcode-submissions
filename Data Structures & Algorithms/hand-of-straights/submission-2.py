class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0 :
            return False

        count = Counter(hand)
        for x in sorted(count):
            n = count[x]                      # groups that must start at x
            if n:
                for y in range(x, x + groupSize):
                    if count[y] < n:
                        return False
                    count[y] -= n
        return True