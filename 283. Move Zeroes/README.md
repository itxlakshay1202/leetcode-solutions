# 283. Move Zeroes

### Difficulty: Easy

## Description
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 
Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:
Input: nums = [0]
Output: [0]

 
Constraints:


	1 <= nums.length <= 104
	-231 <= nums[i] <= 231 - 1


 
Follow up: Could you minimize the total number of operations done?

## Submission Details
- **Status**: Accepted
- **Runtime**: 15
- **Memory**: 13392000
- **Language**: python

## Code
```python
class Solution(object):
    def moveZeroes(self, nums):
        i = 0
        count = 0
        while i < len(nums):
            if nums[i] == 0:
                count += 1
                nums.pop(i)
            else:
                i += 1
        for i in range(0,count):
            nums.append(0)
```
