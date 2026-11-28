# 14. Longest Common Prefix

### Difficulty: Easy

## Description
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 
Example 1:


Input: strs = ["flower","flow","flight"]
Output: "fl"


Example 2:


Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


 
Constraints:


	1 <= strs.length <= 200
	0 <= strs[i].length <= 200
	strs[i] consists of only lowercase English letters if it is non-empty.

## Submission Details
- **Status**: Accepted
- **Runtime**: 3
- **Memory**: 12160000
- **Language**: python

## Code
```python
class Solution(object):
    def longestCommonPrefix(self, strs):
        i = 0
        lst = []
        try:
            while True:
                dic = {}
                for j in strs:
                    if j[i] not in dic and len(dic) == 0:
                        dic[j[i]] = 1
                    elif j[i] not in dic:
                        return "".join(lst)
                    else:
                        dic[j[i]] += 1
                lst.append(j[i])
                i+=1

        except:
            return "".join(lst)
```
