class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0 
        maxFruits = 0
        fruitMap = {}

        for right in range(len(fruits)):
            firstBasket = fruits[right]
            if firstBasket not in fruitMap:
                fruitMap[firstBasket] = 0
            fruitMap[firstBasket] += 1

            while len(fruitMap) > 2:
                secondBasket = fruits[left]
                fruitMap[secondBasket] -= 1
                if fruitMap[secondBasket] == 0:
                    del fruitMap[secondBasket]
                left += 1
            maxFruits = max(maxFruits, right - left + 1)
        return maxFruits
