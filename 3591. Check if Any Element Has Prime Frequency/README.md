# 3591. Check if Any Element Has Prime Frequency

### Difficulty: Easy

## Description
You are given an integer array nums.

Return true if the frequency of any element of the array is prime, otherwise, return false.

The frequency of an element x is the number of times it occurs in the array.

A prime number is a natural number greater than 1 with only two factors, 1 and itself.

 
Example 1:


Input: nums = [1,2,3,4,5,4]

Output: true

Explanation:

4 has a frequency of two, which is a prime number.


Example 2:


Input: nums = [1,2,3,4,5]

Output: false

Explanation:

All elements have a frequency of one.


Example 3:


Input: nums = [2,2,2,4,4]

Output: true

Explanation:

Both 2 and 4 have a prime frequency.


 
Constraints:


	1 <= nums.length <= 100
	0 <= nums[i] <= 100

## Submission Details
- **Status**: Accepted
- **Runtime**: 2
- **Memory**: 11988000
- **Language**: python

## Code
```python
class Solution(object):
    def prime(self , n):
        if n != 2 and n % 2 == 0:
            return False
        p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        i = 0
        while i < len(p) and p[i] <= n:
            if p[i] == n:
                return True
            i+=1
        return False
    def checkPrimeFrequency(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = {}
        for i in nums:
            if i not in dic:
              dic[i] = 1
            else:
                dic[i] += 1

        for i in sorted(dic):
            if self.prime(dic[i]):
                return True

        return False
```
