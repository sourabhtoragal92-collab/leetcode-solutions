from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

# --- Local Testing Block ---
if __name__ == "__main__":
    sol = Solution()
    print(f"Test 1 - Expected: 4, Got: {sol.search([-1, 0, 3, 5, 9, 12], 9)}")
    print(f"Test 2 - Expected: -1, Got: {sol.search([-1, 0, 3, 5, 9, 12], 2)}")
