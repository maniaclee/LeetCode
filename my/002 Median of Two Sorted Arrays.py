"""
There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. The overall
run time complexity should be O(log (m+n)).
"""
__author__ = 'Danyang'


class Solution:
    def findMedianSortedArrays(self, A, B):
        m = len(A)
        n = len(B)
        sum = m + n
        index = sum / 2 if sum & 1 == 0 else(sum / 2 + 1)
        a, b = 0, 0
        while True:
            index -= 1
            if A[a] > B[b]:
                if index == 0:
                    return B[b]
                b += 1
            else:
                if index == 0:
                    return A[a]
                a += 1
            if a == len(A):
                return B[b + index]
            if b == len(B):
                return A[a + index]


if __name__ == "__main__":
    assert Solution().findMedianSortedArrays([1, 2], [1, 2, 3]) == 2
    assert Solution().findMedianSortedArrays([1, 2], [3]) == 2
    assert Solution().findMedianSortedArrays([1], [2, 3]) == 2
    assert Solution().findMedianSortedArrays([1, 2], [1, 2]) == 1.5
