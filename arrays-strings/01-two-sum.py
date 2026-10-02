from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []

# --- Local Testing Block ---
if __name__ == "__main__":
    sol = Solution()
    # Test Case 1: Typical case
    print(f"Test 1 - Expected: [0, 1], Got: {sol.twoSum([2, 7, 11, 15], 9)}")
    # Test Case 2: Negative numbers
    print(f"Test 2 - Expected: [0, 2], Got: {sol.twoSum([-3, 4, 3, 90], 0)}")
