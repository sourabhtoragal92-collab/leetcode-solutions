from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        last_non_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero], nums[i] = nums[i], nums[last_non_zero]
                last_non_zero += 1

# --- Local Testing Block ---
if __name__ == "__main__":
    sol = Solution()
    nums1 = [0, 1, 0, 3, 12]
    sol.moveZeroes(nums1)
    print(f"Test 1 - Expected: [1, 3, 12, 0, 0], Got: {nums1}")
    nums2 = [0]
    sol.moveZeroes(nums2)
    print(f"Test 2 - Expected: [0], Got: {nums2}")
