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

    class Solution(object):
        def findMedianSortedArrays(self, nums1, nums2):
            """
            :type nums1: List[int]
            :type nums2: List[int]
            :rtype: float
            """
            m, n = len(nums1), len(nums2)
            if m > n:
                nums1, nums2, m, n = nums2, nums1, n, m

            imin, imax, half = 0, m, (m + n + 1) // 2
            while imin <= imax:
                # i+j = half
                i = (imin + imax) // 2
                j = half - i

                if i < m and nums1[i] < nums2[j - 1]:
                    # i小
                    imin = i + 1
                elif i > 0 and nums1[i - 1] > nums2[j]:
                    imax = i - 1

                else:
                    if i == 0:
                        max_left = nums2[j - 1]
                    elif j == 0:
                        max_left = nums1[i - 1]
                    else:
                        max_left = max(nums1[i - 1], nums2[j - 1])

                    if (m + n) % 2 == 1:
                        return max_left
                    if i == m:
                        min_right = nums2[j]
                    elif j == n:
                        min_right = nums1[i]
                    else:
                        min_right = min(nums1[i], nums2[j])

                    return (max_left + min_right) / 2.0




