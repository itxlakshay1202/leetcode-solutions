# 744. Find Smallest Letter Greater Than Target

### Difficulty: Easy

## Description
You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

 
Example 1:


Input: letters = ["c","f","j"], target = "a"
Output: "c"
Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.


Example 2:


Input: letters = ["c","f","j"], target = "c"
Output: "f"
Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.


Example 3:


Input: letters = ["x","x","y","y"], target = "z"
Output: "x"
Explanation: There are no characters in letters that is lexicographically greater than 'z' so we return letters[0].


 
Constraints:


	2 <= letters.length <= 104
	letters[i] is a lowercase English letter.
	letters is sorted in non-decreasing order.
	letters contains at least two different characters.
	target is a lowercase English letter.

## Submission Details
- **Status**: Accepted
- **Runtime**: 0 ms
- **Memory**: 13436000
- **Language**: python

## Code
```python
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        si = 0 
        ei = len(letters) - 1

        if ord(target) < ord(letters[si]) or ord(target) >= ord(letters[ei]):
            return letters[0]

        while si < ei:
            mid = si + (ei - si) // 2

            if ord(letters[mid]) <= ord(target):
                si = mid+1
            else:
                ei = mid

        return letters[si]
        
```
