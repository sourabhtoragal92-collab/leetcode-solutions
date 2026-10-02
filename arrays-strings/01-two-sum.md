## Problem: Two Sum (Easy)
**Link:** https://leetcode.com/problems/two-sum/

### Approach
I used a hash map (dictionary) to store each number's value and index as I iterate through the list. For each element, I compute the required complement (`target - num`) and check if it already exists in the map.

### Complexity
- Time: O(n)
- Space: O(n)

### Notes
Using a hash map trades memory for speed, improving time complexity from O(n^2) to O(n).
