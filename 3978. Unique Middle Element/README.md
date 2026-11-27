# 3978. Unique Middle Element

### Difficulty: Easy

## Description
You are given an integer array nums of odd length n.

Return true if the middle element of nums appears exactly once in the array. Otherwise return false.

 
Example 1:


Input: nums = [1,2,3]

Output: true

Explanation:

The middle element of nums is 2, which appears exactly once.

Thus, the answer is true.


Example 2:


Input: nums = [1,2,2]

Output: false

Explanation:

The middle element of nums is 2, which appears twice.

Thus, the answer is false.


 
Constraints:


	1 <= n == nums.length <= 100
	n is odd.
	1 <= nums[i] <= 100

## Submission Details
- **Status**: Accepted
- **Runtime**: 1
- **Memory**: 12260000
- **Language**: python

## Code
```python
class Solution(object):
    def isMiddleElementUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        si = 0
        ei = len(nums)-1
        mid = si + (ei - si) / 2
        if nums.count(nums[mid]) == 1:
            return True
        else:
            return False
```
