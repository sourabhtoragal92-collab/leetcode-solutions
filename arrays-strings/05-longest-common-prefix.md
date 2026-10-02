## Problem: Longest Common Prefix (Easy)
**Link:** https://leetcode.com/problems/longest-common-prefix/

### Approach
Initialized prefix as the first word and dynamically shortened it until all target words matched.

### Complexity
- Time: O(S) where S is total character count
- Space: O(1)

### Notes
Horizontal scanning allows early termination.
