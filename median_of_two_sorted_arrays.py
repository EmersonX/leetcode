class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i, j, nums3, len1, len2 = 0, 0, [], len(nums1), len(nums2)
        while i < len1 and j < len2 and nums1 and nums2:
            if nums1[i] >= nums2[j]:
                nums3.append(nums2[j])
                j += 1
            else:
                nums3.append(nums1[i])
                i += 1

        if i == len1:
            while j < len2:
                nums3.append(nums2[j])
                j += 1
        else:
            while i < len1:
                nums3.append(nums1[i])
                i += 1

        if (i + j) % 2 :
            return nums3[(i+j)/2]
        else:
            return (nums3[(i+j)/2] + nums3[(i+j)/2-1]) * 1.0 /2


if __name__ == '__main__':
    s = Solution()
    nums1 = []
    nums2 = [2, 3]
    print s.findMedianSortedArrays(nums1, nums2)

    nums1 = []
    nums2 = [2]
    print s.findMedianSortedArrays(nums1, nums2)

    nums1 = [1, 2]
    nums2 = [3, 4]
    print s.findMedianSortedArrays(nums1, nums2)

    nums1 = [1, 2]
    nums2 = [3]
    print s.findMedianSortedArrays(nums1, nums2)

    nums1 = [1, 2]
    nums2 = [3, 3, 10]
    print s.findMedianSortedArrays(nums1, nums2)
