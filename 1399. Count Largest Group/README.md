# 1399. Count Largest Group

### Difficulty: Easy

## Description
You are given an integer n.

We need to group the numbers from 1 to n according to the sum of its digits. For example, the numbers 14 and 5 belong to the same group, whereas 13 and 3 belong to different groups.

Return the number of groups that have the largest size, i.e. the maximum number of elements.

 
Example 1:


Input: n = 13
Output: 4
Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
There are 4 groups with largest size.


Example 2:


Input: n = 2
Output: 2
Explanation: There are 2 groups [1], [2] of size 1.


 
Constraints:


	1 <= n <= 104

## Submission Details
- **Status**: Accepted
- **Runtime**: 66
- **Memory**: 12228000
- **Language**: python

## Code
```python
class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        dic = {}
        while i <= n :
            icopy = i
            sum = 0
            while icopy > 0:
                sum += icopy % 10
                icopy //= 10
            if sum not in dic.keys():
                dic[sum] = 1
            else:
                dic[sum] += 1
            i+=1

        max_num = max(dic.values())

        count = 0
        for i in dic.values():
            if i == max_num:
                count+=1
        return count   
```
