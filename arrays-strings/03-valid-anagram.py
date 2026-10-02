from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)

# --- Local Testing Block ---
if __name__ == "__main__":
    sol = Solution()
    print(f"Test 1 - Expected: True, Got: {sol.isAnagram('anagram', 'nagaram')}")
    print(f"Test 2 - Expected: False, Got: {sol.isAnagram('rat', 'car')}")
