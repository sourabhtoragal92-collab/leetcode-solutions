class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack

# --- Local Testing Block ---
if __name__ == "__main__":
    sol = Solution()
    print(f"Test 1 - Expected: True, Got: {sol.isValid('()[]{}')}")
    print(f"Test 2 - Expected: False, Got: {sol.isValid('(]')}")
