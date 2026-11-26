# 1491. Average Salary Excluding the Minimum and Maximum Salary

### Difficulty: Easy

## Description
You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.

 
Example 1:


Input: salary = [4000,3000,1000,2000]
Output: 2500.00000
Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500


Example 2:


Input: salary = [1000,2000,3000]
Output: 2000.00000
Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
Average salary excluding minimum and maximum salary is (2000) / 1 = 2000


 
Constraints:


	3 <= salary.length <= 100
	1000 <= salary[i] <= 106
	All the integers of salary are unique.

## Submission Details
- **Status**: Accepted
- **Runtime**: 0 ms
- **Memory**: 12000000
- **Language**: python

## Code
```python
class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        i = 0
        sum = 0
        min = salary[0]
        max = salary[0]
        while i < len(salary):
            sum+=salary[i]
            if min > salary[i]:
                min = salary[i]
            if max < salary[i]:
                max = salary[i]
            i+=1

        sum -= (min + max)

        return float(sum) / (len(salary) - 2)
```
