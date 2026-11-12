class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        nbOfCoins = [0] * (amount + 1)
        nbOfCoins[0] = 1
        for c in coins : 
            for target in range(1, amount + 1) : 
                if target - c < 0 :
                    continue
                nbOfCoins[target] +=  nbOfCoins[target-c]
      
        return nbOfCoins[amount]