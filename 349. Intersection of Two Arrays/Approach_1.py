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