# 1480. Running Sum of 1d Array

### Difficulty: Easy

## Description
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

 
Example 1:


Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:


Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Example 3:


Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]


 
Constraints:


	1 <= nums.length <= 1000
	-10^6 <= nums[i] <= 10^6

## Submission Details
- **Status**: Accepted
- **Runtime**: 0 ms
- **Memory**: 12264000
- **Language**: python

## Code
```python
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 1
        sum = []
        sum.append(nums[0])
        while i < len(nums):
            sum.append(sum[i-1] + nums[i])
            i+=1
        return sum
```
