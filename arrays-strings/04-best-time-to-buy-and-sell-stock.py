from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit

# --- Local Testing Block ---
if __name__ == "__main__":
    sol = Solution()
    print(f"Test 1 - Expected: 5, Got: {sol.maxProfit([7, 1, 5, 3, 6, 4])}")
    print(f"Test 2 - Expected: 0, Got: {sol.maxProfit([7, 6, 4, 3, 1])}")
