class Solution(object):
    def merge(self, nums1, m, nums2, n):
        for i in range(m,len(nums1)):
            nums1.pop()
        for i in range(n,len(nums2)):
            nums2.pop()

        nums1 += nums2
        nums1.sort()
        return nums1