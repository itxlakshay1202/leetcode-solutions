# 485. Max Consecutive Ones

### Difficulty: Easy

## Description
Given a binary array nums, return the maximum number of consecutive 1's in the array.

 
Example 1:


Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.


Example 2:


Input: nums = [1,0,1,1,0,1]
Output: 2


 
Constraints:


	1 <= nums.length <= 105
	nums[i] is either 0 or 1.

## Submission Details
- **Status**: Accepted
- **Runtime**: 33
- **Memory**: 13536000
- **Language**: python

## Code
```python
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0 
        count = 0
        result = []
        while i < len(nums):
            if nums[i] == 1:
                count += 1
                i += 1
            else:
                result.append(count)
                count = 0
                i += 1
        
        if nums[i-1] == 1:
            result.append(count)
        return max(result)

```
