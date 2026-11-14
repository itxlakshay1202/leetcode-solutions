# 349. Intersection of Two Arrays

### Difficulty: Easy

## Description
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 
Example 1:


Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]


Example 2:


Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.


 
Constraints:


	1 <= nums1.length, nums2.length <= 1000
	0 <= nums1[i], nums2[i] <= 1000

## Submission Details
- **Status**: Accepted
- **Runtime**: 17
- **Memory**: 12392000
- **Language**: python

## Code
```python
class Solution(object):
    def intersection(self, nums1, nums2):
        res = []
        if len(nums1) >= len(nums2):
            for i in range(0,len(nums1)):
                if nums1[i] in nums2 and nums1[i] not in res:
                    res.append(nums1[i]) 
        else :
            for i in range(0,len(nums2)):
                if nums2[i] in nums1 and nums2[i] not in res:
                    res.append(nums2[i])
        return res
```
