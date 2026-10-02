from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

# --- Local Testing Block ---
if __name__ == "__main__":
    sol = Solution()
    print(f"Test 1 - Expected: 'fl', Got: '{sol.longestCommonPrefix(['flower', 'flow', 'flight'])}'")
    print(f"Test 2 - Expected: '', Got: '{sol.longestCommonPrefix(['dog', 'racecar', 'car'])}'")
