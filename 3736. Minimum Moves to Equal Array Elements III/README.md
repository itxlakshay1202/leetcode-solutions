# 3736. Minimum Moves to Equal Array Elements III

### Difficulty: Easy

## Description
You are given an integer array nums.

In one move, you may increase the value of any single element nums[i] by 1.

Return the minimum total number of moves required so that all elements in nums become equal.

 
Example 1:


Input: nums = [2,1,3]

Output: 3

Explanation:

To make all elements equal:


	Increase nums[0] = 2 by 1 to make it 3.
	Increase nums[1] = 1 by 1 to make it 2.
	Increase the updated nums[1] = 2 by 1 to make it 3.


Now, all elements of nums are equal to 3. The minimum total moves is 3.


Example 2:


Input: nums = [4,4,5]

Output: 2

Explanation:

To make all elements equal:


	Increase nums[0] = 4 by 1 to make it 5.
	Increase nums[1] = 4 by 1 to make it 5.


Now, all elements of nums are equal to 5. The minimum total moves is 2.


 
Constraints:


	1 <= nums.length <= 100
	1 <= nums[i] <= 100

## Submission Details
- **Status**: Accepted
- **Runtime**: 1
- **Memory**: 12040000
- **Language**: python

## Code
```python
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        moves = 0
        max = nums[0]
        i = 1
        while i < len(nums):
            if max < nums[i]:
                moves = moves + (i) * (nums[i] - max)
                max = nums[i]
            else:
                moves += (max - nums[i])
            i+=1
        return moves
```
