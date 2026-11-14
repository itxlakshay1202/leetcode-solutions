# 137. Single Number II

### Difficulty: Medium

## Description
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 
Example 1:
Input: nums = [2,2,3,2]
Output: 3
Example 2:
Input: nums = [0,1,0,1,0,1,99]
Output: 99

 
Constraints:


	1 <= nums.length <= 3 * 104
	-231 <= nums[i] <= 231 - 1
	Each element in nums appears exactly three times except for one element which appears once.

## Submission Details
- **Status**: Accepted
- **Runtime**: 890
- **Memory**: 13448000
- **Language**: python

## Code
```python
class Solution(object):
    def singleNumber(self, nums):
        while True:
            i = nums[0]
            if(nums.count(i) == 1):
                return i
            else:
                nums.remove(i)
                nums.remove(i)
                nums.remove(i)
```
