# 219. Contains Duplicate II

### Difficulty: Easy

## Description
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 
Example 1:


Input: nums = [1,2,3,1], k = 3
Output: true


Example 2:


Input: nums = [1,0,1,1], k = 1
Output: true


Example 3:


Input: nums = [1,2,3,1,2,3], k = 2
Output: false


 
Constraints:


	1 <= nums.length <= 105
	-109 <= nums[i] <= 109
	0 <= k <= 105

## Submission Details
- **Status**: Accepted
- **Runtime**: 74
- **Memory**: 28744000
- **Language**: python

## Code
```python
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        i = 0
        while i < len(nums):
            if nums[i] not in dic:
                dic[nums[i]] = i
            else:
                if i - dic[nums[i]] <= k:
                    return True
                else:
                    dic[nums[i]] = i
            i+=1

        return False
```
