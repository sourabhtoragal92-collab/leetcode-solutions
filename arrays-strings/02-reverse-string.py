from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

if __name__ == "__main__":
    sol = Solution()
    s1 = ["h", "e", "l", "l", "o"]
    sol.reverseString(s1)
    print(f"Test 1 - Expected: ['o', 'l', 'l', 'e', 'h'], Got: {s1}")
