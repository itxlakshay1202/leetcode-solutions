# 414. Third Maximum Number

### Difficulty: Easy

## Description
You are given an integer array nums.

Return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

 
Example 1:


Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.


Example 2:


Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.


Example 3:


Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.


 
Constraints:


	1 <= nums.length <= 104
	-231 <= nums[i] <= 231 - 1


 
Follow up: Can you find an O(n) solution?

## Submission Details
- **Status**: Accepted
- **Runtime**: 4
- **Memory**: 12580000
- **Language**: python

## Code
```python
class Solution(object):
    def thirdMax(self, nums):
        largest = []
        i = 0
        while i < len(nums):
            if nums[i] not in largest:
                if len(largest) == 0:
                    largest.append(nums[i])
                elif len(largest) == 1:
                    if nums[i] < largest[0]:
                        largest.insert(0, nums[i])
                    else:
                        largest.append(nums[i])
                elif len(largest) == 2:
                    if nums[i] < largest[0]:
                        largest.insert(0, nums[i])
                    elif nums[i] < largest[1]:
                        largest.insert(1, nums[i])
                    else:
                        largest.append(nums[i])
                else:
                    if nums[i] > largest[0]:
                        largest.pop(0)
                        if nums[i] < largest[0]:
                            largest.insert(0, nums[i])
                        elif nums[i] < largest[1]:
                            largest.insert(1, nums[i])
                        else:
                            largest.append(nums[i])
            i += 1

        if len(largest) == 3:
            return largest[0]
        else:
            return max(largest)
```
