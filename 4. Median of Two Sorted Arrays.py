class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        ans = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                ans.append(nums1[i])
                i += 1
            else:
                ans.append(nums2[j])
                j += 1
        if i < len(nums1):
            ans.extend(nums1[i:])
        if j < len(nums2):
            ans.extend(nums2[j:])

        n = len(ans) // 2
        m = (len(ans) - 1) // 2
        mid = (ans[n] + ans[m]) / 2.0
        return mid