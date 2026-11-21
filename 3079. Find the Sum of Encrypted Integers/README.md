# 3079. Find the Sum of Encrypted Integers

### Difficulty: Easy

## Description
You are given an integer array nums containing positive integers. We define a function encrypt such that encrypt(x) replaces every digit in x with the largest digit in x. For example, encrypt(523) = 555 and encrypt(213) = 333.

Return the sum of encrypted elements.

 
Example 1:


Input: nums = [1,2,3]

Output: 6

Explanation: The encrypted elements are [1,2,3]. The sum of encrypted elements is 1 + 2 + 3 == 6.


Example 2:


Input: nums = [10,21,31]

Output: 66

Explanation: The encrypted elements are [11,22,33]. The sum of encrypted elements is 11 + 22 + 33 == 66.


 
Constraints:


	1 <= nums.length <= 50
	1 <= nums[i] <= 1000

## Submission Details
- **Status**: Accepted
- **Runtime**: 32
- **Memory**: 12060000
- **Language**: python

## Code
```python
class Solution(object):
    def encrypt(self , n):
        count = 0
        max = 0
        while n > 0:
            if n % 10 > max:
                max = n % 10
            
            count +=1
            n //= 10

        while count > 0:
            n = n * 10 + max
            count -= 1

        return n

    def sumOfEncryptedInt(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        for i in nums:
            sum += self.encrypt(i)

        return sum
        
```
